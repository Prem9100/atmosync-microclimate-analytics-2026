# Week 2 Day 8 – Python Kafka Producer Validation

Date: 20 November 2026  
Member 2 – Python & Kafka Producer

## Validation Performed

- Python test suite executed successfully.
- Result: 6 tests passed.
- Docker Compose services started successfully.
- Kafka producer connected successfully.
- Producer delivered telemetry to the tmosync.sensor.telemetry topic.
- Newly generated records were delivered at offsets 148–149.
- Kafka consumer successfully read 2 messages starting from offset 148.
- Verified telemetry fields:
  - event_id
  - event_ts
  - container_id
  - commodity
  - temperature_c
  - humidity_pct
  - vibration_g
  - quantity_kg

## Result

Week 2 Day 8 Python and Kafka producer validation completed successfully. The producer generated valid telemetry and the records were successfully delivered to and consumed from Kafka.
