# Week 2 Kafka Integration Validation

## Project
AtmoSync: Micro-Climate Arbitrage Analytics

## Member
Member 1 - Team Lead & Kafka Integration

## Week
Week 2

## Objective
Validate and document the end-to-end telemetry flow from the Python simulator through Apache Kafka and into the downstream analytics pipeline.

## Kafka Configuration

- Kafka Broker: localhost:9092
- Kafka Topic: atmosync.sensor.telemetry
- Kafka Partition: 0
- Message Key: container_id
- Message Format: JSON

## Telemetry Fields

Each telemetry event contains:

- event_id
- event_ts
- container_id
- commodity
- temperature_c
- humidity_pct
- vibration_g
- quantity_kg

## Verified Data Flow

Python Simulator
        |
        v
Kafka Producer
        |
        v
Apache Kafka
        |
        v
atmosync.sensor.telemetry
        |
        v
Snowflake Consumer
        |
        v
ATMOSYNC_DB.RAW.SENSOR_EVENTS
        |
        v
dbt Staging
        |
        v
dbt Analytics
        |
        v
Apache Superset

## Kafka Validation

The Kafka producer was successfully tested during Week 2.

The producer successfully generated telemetry events and published them to the Kafka topic.

The Kafka delivery callback confirmed successful message delivery.

The verified Kafka partition was:

Partition: 0

Multiple delivery offsets were observed during testing, confirming that telemetry messages were being accepted by Kafka.

## Consumer Validation

A Kafka consumer was used to verify that messages published to the topic could be consumed successfully.

The consumer successfully processed 54 telemetry messages during validation.

This confirmed the following flow:

Python Simulator -> Kafka Producer -> Kafka Topic -> Kafka Consumer

## Producer Improvements

The Kafka producer was improved during Week 2.

The producer now includes:

- Dedicated producer creation function
- Structured Kafka configuration
- Delivery callback handling
- Detailed telemetry logging
- Exception handling
- Graceful shutdown
- Final message flushing

The producer logs important telemetry information including:

- Event ID
- Container ID
- Commodity
- Temperature
- Humidity
- Vibration
- Quantity

## Integration Status

Kafka integration is working successfully.

The Week 2 validation confirmed:

1. Python telemetry generation is working.
2. Kafka producer is working.
3. Kafka broker is reachable on localhost:9092.
4. The required Kafka topic exists.
5. Telemetry messages are successfully delivered.
6. Kafka messages can be consumed successfully.
7. The telemetry structure is compatible with the downstream Snowflake pipeline.
8. Member 2's Kafka producer improvements were committed and merged into the main branch.

## Team Lead Responsibility

As Team Lead and Kafka Integration member, my responsibilities include:

- Managing the GitHub repository.
- Maintaining the Member 1 branch.
- Coordinating Kafka integration.
- Reviewing member contributions.
- Merging completed member branches into main.
- Verifying end-to-end project integration.
- Maintaining project documentation.
- Tracking Week 2 progress.

## Week 2 Result

Kafka telemetry integration has been successfully validated.

The AtmoSync pipeline can generate simulated micro-climate telemetry, publish it to Apache Kafka, consume the messages, and continue the data flow toward Snowflake, dbt, and Superset analytics.

## Conclusion

The Week 2 Kafka integration work confirms that the messaging layer of the AtmoSync architecture is operational.

The validated architecture is:

Python Simulator -> Kafka Producer -> Apache Kafka -> Snowflake Consumer -> Snowflake RAW -> dbt Analytics -> Superset
