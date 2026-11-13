# Week 2 Python & Kafka Validation

## Objective

Validate the Python telemetry simulator and Kafka producer integration for the AtmoSync project.

## Environment

- Python: 3.x
- Kafka: Apache Kafka 4.1.2
- Kafka bootstrap server: `localhost:9092`
- Kafka topic: `atmosync.sensor.telemetry`
- Kafka partitions: 1
- Replication factor: 1

## Validation Performed

### 1. Python Simulator Tests

Command:

```bash
python -m pytest -q