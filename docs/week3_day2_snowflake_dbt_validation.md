# Week 3 Day 2 - Snowflake dbt Arbitrage Validation

## Objective

Strengthen validation of the Week 3 commodity arbitrage analytics
model using an additional dbt data-quality test.

## Model

Model:
commodity_arbitrage_analytics

The model combines:
- Commodity prices
- Source and destination market prices
- Sensor telemetry
- Sensor risk information
- Shipment quantity

## Additional Validation

Added:

tests/test_commodity_arbitrage_status.sql

The test verifies that ARBITRAGE_STATUS contains only the expected
values:

- OPPORTUNITY
- HIGH_RISK
- NO_OPPORTUNITY
- NO_SENSOR_DATA

## dbt Test Result

Command:

dbt test --project-dir atmosync_dbt --select commodity_arbitrage_analytics

Result:

PASS=9
WARN=0
ERROR=0
SKIP=0
NO-OP=0
REUSED=0
TOTAL=9

All nine selected data tests passed successfully.

## Data Quality

The existing not-null tests also passed for:
- PRICE_DATE
- COMMODITY
- SOURCE_MARKET
- DESTINATION_MARKET
- SOURCE_PRICE_PER_KG
- DESTINATION_PRICE_PER_KG
- PRICE_DIFFERENCE_PER_KG
- ARBITRAGE_STATUS

## Note

dbt reported an existing CustomKeyInConfigDeprecation warning in
dbt_project.yml. This warning did not cause any test failure.

## Week 3 Day 2 Status

Commodity arbitrage analytics validation completed successfully.
