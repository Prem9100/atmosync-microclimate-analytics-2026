# Week 2 Day 6 – Superset Dashboard Validation

## Date
18 November 2026

## Member
Member 4 – Superset / BI

## Validation Performed

### 1. Superset Service Validation
Docker Compose was started successfully.

Running services:
- atmosync-kafka
- atmosync-superset

### 2. AtmoSync Dashboard Validation
The AtmoSync Micro-Climate Analytics dashboard was opened successfully in Apache Superset.

### 3. Snowflake Permission Validation
The dashboard initially displayed SQL access control errors for the table:
ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS

The required SELECT permission was granted to the SYSADMIN role.

### 4. Dashboard Chart Validation
The following charts were successfully displayed:
- Commodity Alert Events
- Vibration Alert Status
- Temperature Alert Status
- Humidity Alert Status

The dashboard displayed telemetry analytics for:
- Avocado
- Banana
- Mango

The alert-status charts displayed HIGH and NORMAL categories.

### 5. Refresh Validation
The Superset dashboard was refreshed in the browser.
After refresh, the dashboard continued to load successfully and the charts remained populated with data.

## Conclusion
The AtmoSync Superset dashboard was successfully validated for Week 2 Day 6. Snowflake access permissions were verified, the dashboard charts loaded correctly, and the dashboard remained functional after a browser refresh.
