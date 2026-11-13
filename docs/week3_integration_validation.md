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
