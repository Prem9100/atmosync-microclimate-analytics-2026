# Week 2 Final Review – Snowflake & dbt

Date: 23 November 2026
Team: AtmoSync Micro-Climate Analytics

## Week 2 Final Objective

Complete the final validation of the Snowflake and dbt data transformation pipeline and confirm that the required models and data-quality tests execute successfully.

## Final Snowflake Validation

- Snowflake connection validated successfully through dbt debug.
- Connection test returned [OK connection ok].
- ATMOSYNC_DB database and RAW schema were successfully accessed.
- dbt project configuration and profiles were validated.

## Final dbt Build Validation

The final dbt build completed successfully.

- 2 models discovered
- 1 source discovered
- 12 data tests executed
- 1 view model created successfully
- 1 table model created successfully
- 14 total validations completed
- PASS: 14
- WARN: 0
- ERROR: 0
- SKIP: 0
- NO-OP: 0
- REUSED: 0

## Data Quality Validation

The dbt tests validated:

- Risk level accepted values
- Risk score accepted values
- Overall status accepted values
- Humidity status accepted values
- Temperature status accepted values
- Vibration status accepted values
- Event ID not-null validation
- Event timestamp not-null validation
- Risk level not-null validation
- Risk score not-null validation
- Sensor telemetry range validation
- Event ID uniqueness validation

All 12 data tests passed successfully.

## Warning

The dbt build reported one deprecation warning related to the custom "atmosync_dbt" configuration key in dbt_project.yml.

This warning did not cause a build failure. The build completed successfully with 14/14 validations passed.

## Week 2 Conclusion

The Snowflake and dbt pipeline successfully completed the final Week 2 validation. The required models were created and all data-quality tests passed.

Member 3's Week 2 responsibilities are complete and the Snowflake/dbt pipeline is ready for the next planned development phase.
