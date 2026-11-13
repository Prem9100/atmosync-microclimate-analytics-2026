# Week 2 Snowflake and dbt Validation

## Objective

Validate the AtmoSync Snowflake and dbt data pipeline and confirm that the staging and analytics models, source configuration, and data-quality tests execute successfully.

## Environment

- Python: 3.13.13
- dbt Core: 1.13.0-rc1
- dbt Snowflake Adapter: 1.12.5
- Database: Snowflake
- dbt Project: `atmosync_dbt`

## 1. dbt Connection Validation

The dbt environment was validated using:

```bash
dbt debug