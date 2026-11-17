# Week 2 Day 5 - Superset Dashboard Validation

## Date
17 November 2026

## Objective
Validate the AtmoSync Superset dashboard after fresh Kafka telemetry generation and confirm that the dashboard can access the Snowflake analytics data.

## Validation Performed

### 1. Superset Services
Docker Compose successfully started:
- atmosync-kafka
- atmosync-superset

### 2. Dashboard Access
The AtmoSync Micro-Climate Analytics dashboard was opened successfully in Apache Superset.

### 3. Snowflake Permission Validation
The dashboard initially displayed SQL access control errors for:
ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS

The required SELECT permission was granted to the SYSADMIN role.

After refreshing the dashboard, the charts loaded successfully.

### 4. Dashboard Charts Validated
The following charts were successfully displayed:
- Commodity Alert Events
- Vibration Alert Status
- Temperature Alert Status
- Humidity Alert Status

The dashboard displayed commodity categories including Avocado, Banana, and Mango, and the alert status charts displayed their corresponding results.

## Result
The AtmoSync Superset dashboard was successfully validated after resolving the Snowflake SELECT permission issue. The dashboard can access the SENSOR_EVENTS_ANALYTICS table and display the expected analytics visualizations.

## Member 4 Status
Superset dashboard validation completed for Week 2 Day 5.
