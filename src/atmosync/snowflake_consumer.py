
import json
import logging
from pathlib import Path

from confluent_kafka import Consumer, KafkaException
import snowflake.connector

from .config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    KAFKA_GROUP_ID,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_USER,
    SNOWFLAKE_PRIVATE_KEY_PATH,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
    SNOWFLAKE_ROLE,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

INSERT_SQL = """
INSERT INTO SENSOR_EVENTS
(
    EVENT_ID,
    EVENT_TS,
    CONTAINER_ID,
    COMMODITY,
    TEMPERATURE_C,
    HUMIDITY_PCT,
    VIBRATION_G,
    QUANTITY_KG
)
SELECT %s, %s::TIMESTAMP_TZ, %s, %s, %s, %s, %s, %s
"""


def main():
    required = {
        "SNOWFLAKE_ACCOUNT": SNOWFLAKE_ACCOUNT,
        "SNOWFLAKE_USER": SNOWFLAKE_USER,
    }

    missing = [name for name, value in required.items() if not value]

    if missing:
        raise RuntimeError(
            "Missing configuration variables: " + ", ".join(missing)
        )

    private_key = Path(SNOWFLAKE_PRIVATE_KEY_PATH)

    if not private_key.is_file():
        raise FileNotFoundError(
            f"Snowflake RSA private key not found: {private_key}"
        )

    conn = snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        private_key_file=str(private_key),
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE,
    )

    cursor = conn.cursor()

    consumer = Consumer({
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "group.id": KAFKA_GROUP_ID,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False,
    })

    consumer.subscribe([KAFKA_TOPIC])

    logging.info(
        "Consuming Kafka topic %s and writing to Snowflake",
        KAFKA_TOPIC
    )

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                raise KafkaException(msg.error())

            event = json.loads(msg.value().decode("utf-8"))

            values = (
                event["event_id"],
                event["event_ts"],
                event["container_id"],
                event["commodity"],
                event["temperature_c"],
                event["humidity_pct"],
                event["vibration_g"],
                event["quantity_kg"],
            )

            cursor.execute(INSERT_SQL, values)
            conn.commit()

            consumer.commit(message=msg, asynchronous=False)

            logging.info("Inserted sensor event %s", event["event_id"])

    except KeyboardInterrupt:
        logging.info("Stopping Snowflake consumer")

    finally:
        consumer.close()
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
