# Week 2 Day 5 - Kafka End-to-End Validation

## Date
17 November 2026

## Objective
Validate Kafka telemetry generation and consumption as part of the AtmoSync pipeline.

## Validation Performed

### 1. Kafka Services
Docker Compose successfully started:
- atmosync-kafka
- atmosync-superset

### 2. Kafka Producer
The AtmoSync Kafka producer was executed successfully.

Kafka broker:
localhost:9092

Kafka topic:
atmosync.sensor.telemetry

The producer successfully delivered telemetry messages to partition 0.

Validated offsets:
338 through 356

The producer completed the Kafka flush operation successfully and stopped cleanly.

### 3. Kafka Consumer
Kafka Console Consumer was used to read messages beginning at offset 338.

Five messages were successfully consumed and verified.

### 4. Telemetry Schema Validation
The consumed messages contained the expected fields:
- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

## Result
Kafka producer and consumer validation passed successfully. Fresh simulated sensor telemetry was successfully produced, delivered to the AtmoSync Kafka topic, and consumed from the Kafka partition.

## Team Lead Status
Member 1 Kafka validation completed for Week 2 Day 5. The result will be used as evidence for the ongoing end-to-end AtmoSync pipeline integration.
