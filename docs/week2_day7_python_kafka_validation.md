# Week 2 Day 7 – Python Kafka Validation

## Date
19 November 2026

## Member
Member 2 – Python & Kafka Producer

## Validation Performed

### 1. Python Test Validation
The Python test suite was executed successfully.

Test result:
- 6 tests passed

### 2. Kafka Producer Validation
The AtmoSync Python Kafka producer was executed successfully after starting the Kafka service.

The producer generated telemetry and successfully delivered messages to the atmosync.sensor.telemetry topic.

Successfully delivered messages reached partition 0 offsets 131–132.

### 3. Kafka Consumer Validation
Two newly produced telemetry messages were successfully read back from Kafka starting at offset 131.

The consumed messages contained the expected telemetry fields:
- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

### Conclusion
Week 2 Day 7 Python and Kafka validation was completed successfully. The Python test suite passed, the Kafka producer successfully delivered telemetry, and the produced messages were successfully consumed from the Kafka topic with the expected telemetry structure.
