# Superset Dashboard

## Dashboard
AtmoSync Micro-Climate Analytics

## Database
Snowflake

## Dataset
RAW.SENSOR_EVENTS_ANALYTICS

## Charts
1. Commodity Alert Events
2. Vibration Alert Status
3. Humidity Alert Status
4. Temperature Alert Status

## Purpose
The Superset dashboard provides visual analytics for the AtmoSync
micro-climate telemetry data. The charts help monitor commodity alerts,
vibration conditions, humidity conditions, and temperature conditions.

## Data Flow
Python Simulator -> Kafka -> Snowflake RAW -> dbt Analytics -> Superset

## Superset
Superset runs locally on port 8088.
