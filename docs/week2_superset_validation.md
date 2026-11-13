# Week 2 Superset Dashboard Validation

## Objective

Validate the AtmoSync Superset dashboard with the Snowflake analytics table and confirm that dashboard charts can retrieve current analytics data.

## Validation Performed

### 1. Superset Environment

- Superset dashboard: `AtmoSync Micro-Climate Analytics`
- Superset running through Docker
- Dashboard successfully opened at `http://localhost:8088`

### 2. Initial Issue

The dashboard initially displayed SQL access-control errors for:

`ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS`

The error indicated that the Superset database role did not have SELECT permission on the analytics table.

### 3. Snowflake Permission Fix

The required permission was granted:

```sql
GRANT SELECT ON TABLE ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS
TO ROLE SYSADMIN;
```

The permission was verified using:

```sql
SHOW GRANTS ON TABLE ATMOSYNC_DB.RAW.SENSOR_EVENTS_ANALYTICS;
```

The result confirmed SELECT access for SYSADMIN.

### 4. Dashboard Validation

After refreshing the Superset dashboard, the charts successfully loaded data.

Validated dashboard charts include:

- Commodity Alert Events
- Vibration Alert Status
- Temperature Alert Status
- Humidity Alert Status
- Overall Alert Status

### Week 2 Result

The Superset dashboard successfully retrieves analytics data from Snowflake after correcting the required table permission.

## Data Flow

Python Simulator  
→ Kafka  
→ Snowflake RAW  
→ dbt Analytics  
→ Superset Dashboard

## Conclusion

Member 4's Week 2 Superset validation was completed successfully. The dashboard is connected to the Snowflake analytics layer and is displaying analytics results.