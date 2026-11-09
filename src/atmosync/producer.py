import json
import logging
import time
from confluent_kafka import Producer
from .config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, SIMULATOR_INTERVAL_SECONDS
from .simulator import generate_event

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def delivery_report(error, message):
    if error:
        logging.error("Delivery failed: %s", error)
    else:
        logging.info("Kafka delivered topic=%s partition=%s offset=%s",
                     message.topic(), message.partition(), message.offset())

def main():
    producer = Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})
    logging.info("Publishing to %s", KAFKA_TOPIC)
    try:
        while True:
            event = generate_event()
            producer.produce(
                KAFKA_TOPIC,
                key=event["container_id"],
                value=json.dumps(event),
                callback=delivery_report,
            )
            producer.poll(0)
            logging.info("Generated %s | %.2f C | %.2f%% RH",
                         event["container_id"], event["temperature_c"], event["humidity_pct"])
            time.sleep(SIMULATOR_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logging.info("Stopping producer")
    finally:
        producer.flush(10)

if __name__ == "__main__":
    main()
