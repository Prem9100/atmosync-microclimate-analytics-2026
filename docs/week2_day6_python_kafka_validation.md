# Week 2 Day 6 – Python Kafka Validation

## Date
18 November 2026

## Member
Member 2 – Python / Kafka Producer

## Validation Performed

### 1. Python Test Validation
The Python test suite was executed successfully.

Result:
6 tests passed.

### 2. Kafka Service Validation
Docker Compose was started successfully with the AtmoSync Kafka service.

### 3. Python Kafka Producer Validation
The Python Kafka producer was executed successfully using:
python -m src.atmosync.producer

The producer generated telemetry and successfully delivered messages to the atmosync.sensor.telemetry Kafka topic.

Telemetry included:
- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

### 4. Kafka Consumer Validation
The Kafka console consumer successfully read 5 messages from the atmosync.sensor.telemetry topic.

The consumed messages contained the expected telemetry fields and valid sensor values.

### Conclusion
Week 2 Day 6 Python and Kafka validation was completed successfully. The Python tests passed, the producer delivered telemetry to Kafka, and the Kafka consumer successfully read the generated telemetry messages.
