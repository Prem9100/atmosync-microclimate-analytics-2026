# Week 3 Day 3 - Snowflake dbt Price Difference Validation

## Objective

Validate the calculation logic used by the Week 3 commodity arbitrage analytics model.

## New dbt Test

Test file:

atmosync_dbt/tests/test_commodity_price_difference.sql

The test verifies that:

PRICE_DIFFERENCE_PER_KG = DESTINATION_PRICE_PER_KG - SOURCE_PRICE_PER_KG

Any record that does not satisfy this calculation is returned as a test failure.

## Test Execution

Command:

dbt test --project-dir atmosync_dbt --select commodity_arbitrage_analytics

## Result

All 10 selected data tests passed successfully.

PASS=10
WARN=0
ERROR=0
SKIP=0
NO-OP=0
REUSED=0
TOTAL=10

The new test_commodity_price_difference test passed.

The existing test_commodity_arbitrage_status test also passed.

## Validation Coverage

The selected dbt tests validated:

- Required commodity arbitrage fields are not null.
- Arbitrage status values are valid.
- Price difference calculation is correct.
- Source and destination price fields are populated.
- Source and destination markets are populated.

## Warning

dbt reported the existing CustomKeyInConfigDeprecation warning related to the custom configuration key in dbt_project.yml.

The warning did not affect the successful test execution.

## Status

Week 3 Day 3 Snowflake/dbt price difference validation completed successfully.
