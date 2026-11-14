# Week 2 Day 3 Superset Dashboard Validation

## Objective

Validate the AtmoSync Superset dashboard after confirming Snowflake permissions and ensure that the analytics charts can successfully retrieve and display data.

## Superset Environment

- Superset: Apache Superset
- Running through Docker
- Dashboard: AtmoSync Micro-Climate Analytics
- URL: http://localhost:8088

## Initial Validation Issue

The dashboard initially displayed SQL access-control errors for:

`ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS`

The error indicated that the Superset database role did not have sufficient SELECT privileges on the analytics table.

## Snowflake Permission Validation

The required permission was granted:

```sql
GRANT SELECT ON TABLE ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS
TO ROLE SYSADMIN;