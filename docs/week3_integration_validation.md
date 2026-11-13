# Week 3 Integration Validation

## Project
AtmoSync: Micro-Climate Arbitrage Analytics

## Member 1 Responsibility
Team Lead and Kafka Integration

## Week 3 Objective
Validate that the Week 3 risk-scoring analytics developed by the
Snowflake/dbt workstream are integrated into the overall AtmoSync pipeline.

## End-to-End Architecture

Python Simulator
    |
    v
Kafka Producer
    |
    v
Apache Kafka
Topic: atmosync.sensor.telemetry
    |
    v
Snowflake RAW.SENSOR_EVENTS
    |
    v
dbt Staging
    |
    v
dbt Analytics
    |
    +--> RISK_SCORE
    |
    +--> RISK_LEVEL
    |
    v
Superset Dashboard

## Kafka Integration

Kafka bootstrap server:
localhost:9092

Telemetry topic:
atmosync.sensor.telemetry

Kafka message key:
container_id

The telemetry message contains:
- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

## Week 3 Risk Analytics

The dbt analytics model now calculates:

### RISK_SCORE
Risk score ranges from 0 to 3.

Risk points are assigned for:
- Temperature outside the defined safe range
- Humidity outside the defined safe range
- Vibration above the defined threshold

### RISK_LEVEL

0 points -> LOW
1 point  -> MEDIUM
2-3 points -> HIGH

## Validation Performed

The dbt build was executed successfully.

Result:
PASS=14
WARN=0
ERROR=0
SKIP=0
NO-OP=0
REUSED=0
TOTAL=14

The validation included:
- Risk score accepted-value validation
- Risk score not-null validation
- Risk level accepted-value validation
- Risk level not-null validation
- Existing telemetry range validation
- Existing event ID and timestamp validation
- Existing alert-status validations

## Integration Status

Kafka telemetry pipeline:
VALIDATED

Snowflake RAW ingestion:
VALIDATED

dbt staging:
VALIDATED

dbt analytics:
VALIDATED

Week 3 risk scoring:
VALIDATED

Superset:
READY FOR RISK ANALYTICS UPDATE

## Team Lead Responsibilities

Member 1 coordinates the integration between:
- Member 2: Python simulator and Kafka producer
- Member 3: Snowflake and dbt analytics
- Member 4: Superset dashboard
- Member 1: Kafka, GitHub integration, validation, coordination, and merging

## Conclusion

The Week 3 dbt risk-scoring changes are successfully available in the
main integration branch. The analytics model produces validated
RISK_SCORE and RISK_LEVEL fields. The next integration activity is to
update the Superset dashboard to visualize these risk metrics.

## Kafka Runtime Validation

The Kafka broker was started successfully using the
apache/kafka:4.1.2 container image.

The telemetry topic was verified with the Kafka topic CLI.

Topic:
atmosync.sensor.telemetry

Configuration:
- Partition count: 1
- Replication factor: 1
- Leader: 1
- In-sync replica: 1
- Minimum in-sync replicas: 1

A Kafka console consumer was then used to read three telemetry messages
from the topic. The messages contained the expected AtmoSync telemetry
schema, including event ID, timestamp, container ID, commodity,
temperature, humidity, vibration, and quantity.

Three messages were successfully processed:

- Avocado / CONT_004
- Mango / CONT_002
- Avocado / CONT_004

Result:
Kafka broker availability: PASS
Kafka topic availability: PASS
Kafka telemetry consumption: PASS
Telemetry schema validation: PASS

## Snowflake RAW Table Runtime Validation

On 13 November 2026, the Snowflake consumer was executed successfully using:

python -m src.atmosync.snowflake_consumer

The consumer connected to Snowflake and consumed telemetry from the Kafka topic atmosync.sensor.telemetry.

Three new sensor events were inserted successfully:
- 2d3cd2c1-6216-4a4c-99ce-a2052886138a
- 79b1dba8-5038-4911-941b-c9250aadc96a
- e75a6473-432d-482a-ae2f-4f9eb137c1fd

The Snowflake query against ATMOSYNC_DB.RAW.SENSOR_EVENTS returned the latest telemetry records with populated:
- EVENT_ID
- EVENT_TS
- CONTAINER_ID
- COMMODITY
- TEMPERATURE_C
- HUMIDITY_PCT
- VIBRATION_G
- QUANTITY_KG

This confirms that the Kafka-to-Snowflake ingestion path is operational and that telemetry is being persisted in the RAW layer for downstream dbt analytics.
