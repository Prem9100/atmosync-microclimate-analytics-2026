import json
import logging
import time

from confluent_kafka import Producer

from .config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    SIMULATOR_INTERVAL_SECONDS,
)

from .simulator import generate_event


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


def delivery_report(error, message):
    """Handle Kafka message delivery result."""

    if error is not None:
        logger.error("Kafka delivery failed: %s", error)
        return

    logger.info(
        "Kafka delivered topic=%s partition=%s offset=%s",
        message.topic(),
        message.partition(),
        message.offset(),
    )


def create_producer():
    """Create and return Kafka producer."""

    configuration = {
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "client.id": "atmosync-python-producer",
    }

    return Producer(configuration)


def publish_event(producer, event):
    """Publish one telemetry event to Kafka."""

    payload = json.dumps(event)

    producer.produce(
        topic=KAFKA_TOPIC,
        key=event["container_id"],
        value=payload,
        callback=delivery_report,
    )

    producer.poll(0)


def main():
    """Generate and continuously publish telemetry."""

    producer = create_producer()

    logger.info("Starting AtmoSync Kafka producer")
    logger.info("Kafka broker: %s", KAFKA_BOOTSTRAP_SERVERS)
    logger.info("Kafka topic: %s", KAFKA_TOPIC)
    logger.info(
        "Simulation interval: %s seconds",
        SIMULATOR_INTERVAL_SECONDS,
    )

    try:
        while True:
            event = generate_event()

            publish_event(
                producer,
                event,
            )

            logger.info(
                "Generated event_id=%s | "
                "container=%s | "
                "commodity=%s | "
                "temperature=%.2f C | "
                "humidity=%.2f%% | "
                "vibration=%.2f g | "
                "quantity=%.2f kg",
                event["event_id"],
                event["container_id"],
                event["commodity"],
                event["temperature_c"],
                event["humidity_pct"],
                event["vibration_g"],
                event["quantity_kg"],
            )

            time.sleep(SIMULATOR_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        logger.info("Stopping AtmoSync Kafka producer...")

    except Exception as error:
        logger.exception(
            "Producer stopped because of error: %s",
            error,
        )

    finally:
        logger.info("Flushing remaining Kafka messages...")

        producer.flush(10)

        logger.info("AtmoSync Kafka producer stopped.")


if __name__ == "__main__":
    main()
