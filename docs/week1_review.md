# AtmoSync – Week 1 Review

## 1. Project Title

AtmoSync: Micro-Climate Arbitrage Analytics

## 2. Project Objective

AtmoSync is designed to monitor micro-climate conditions in agricultural shipping containers using sensor telemetry and analyze the collected data for operational and commodity-related insights.

The project focuses on temperature, humidity, vibration, container information, commodity information, and quantity data.

## 3. Week 1 Architecture

The Week 1 data pipeline is:

Python Simulator
↓
Apache Kafka
↓
Snowflake RAW
↓
dbt Staging
↓
dbt Analytics
↓
Apache Superset

## 4. Technologies Used

- Python
- Apache Kafka
- Snowflake
- dbt
- Apache Superset
- GitHub
- Docker
- SQL

## 5. Team Responsibilities

### Member 1 – Team Lead / Kafka

Responsibilities:

- Team coordination
- GitHub repository and branch management
- Kafka integration
- Telemetry contract
- Integration monitoring
- Reviewing and merging member branches
- Maintaining the main branch
- Week 1 integration review

### Member 2 – Python

Responsibilities:

- Python simulator
- Sensor telemetry generation
- Simulator validation
- Python tests
- Kafka producer-related development

### Member 3 – Snowflake / dbt

Responsibilities:

- Snowflake data layer
- RAW data validation
- dbt staging model
- dbt analytics model
- Data transformation
- Analytics alert thresholds

### Member 4 – Superset

Responsibilities:

- Apache Superset setup
- Snowflake connection
- Dataset configuration
- Dashboard development
- Analytics visualization

## 6. Kafka Integration

Kafka is used as the messaging layer between telemetry generation and downstream processing.

Kafka topic:

`atmosync.sensor.telemetry`

The telemetry contract contains:

- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

The Kafka message key is:

`container_id`

## 7. Snowflake Integration

Snowflake is used as the data storage and processing layer.

The main database is:

`ATMOSYNC_DB`

The RAW schema contains the sensor telemetry data.

Main RAW table:

`SENSOR_EVENTS`

The Snowflake layer receives the telemetry data from the Kafka processing pipeline.

## 8. dbt Transformation

dbt is used to transform RAW telemetry into analytics-ready data.

### Staging Model

`stg_sensor_events`

The staging model selects the required telemetry fields from the RAW sensor events table.

### Analytics Model

`sensor_events_analytics`

The analytics model calculates sensor alert statuses and an overall alert status.

The Week 1 thresholds were aligned with the simulator telemetry ranges.

## 9. Superset Dashboard

The Superset dashboard is:

`AtmoSync Micro-Climate Analytics`

The dashboard uses the analytics data produced by the dbt layer.

The dashboard supports monitoring of:

- Temperature conditions
- Humidity conditions
- Vibration conditions
- Commodity alert events
- Alert status distribution

## 10. GitHub Workflow

The project uses a shared GitHub repository with separate branches for each team member.

Branches:

- member-1-teamlead-kafka
- member-2-python
- member-3-snowflake-dbt
- member-4-superset
- main

The Team Lead reviews member branches and merges completed work into `main`.

## 11. Week 1 GitHub Integration

During Week 1, the team completed meaningful work across the project branches.

Member 1:
- Kafka telemetry contract

Member 2:
- Simulator telemetry validation tests

Member 3:
- dbt analytics alert threshold alignment

Member 4:
- Superset dashboard documentation

The completed work was reviewed and merged into the main branch.

## 12. Problems Encountered

During Week 1, the team encountered issues related to:

- Git branch synchronization
- Merge management
- Superset initialization
- Snowflake permissions
- dbt model validation
- Python test environment setup

These issues were resolved during the integration process.

## 13. Current Week 1 Status

The Week 1 project structure and primary analytics pipeline are established.

The current architecture is:

Python Simulator
↓
Kafka
↓
Snowflake RAW
↓
dbt Staging
↓
dbt Analytics
↓
Superset

The four team members have completed their assigned Week 1 responsibilities and their work has been integrated into the main branch.

## 14. Week 2 Direction

Week 2 will focus on extending the working pipeline and improving the analytics capabilities of AtmoSync.

Planned areas include:

- Further telemetry processing
- Data quality improvements
- Analytics enhancement
- Dashboard enhancement
- Commodity-related analysis
- Integration testing
- Documentation
- Project validation

## 15. Conclusion

Week 1 established the core technical foundation of AtmoSync.

The team successfully created the initial telemetry pipeline, established Kafka messaging, connected the data flow to Snowflake, implemented dbt transformations, and created the Superset analytics layer.

The project is ready for the next development phase.
