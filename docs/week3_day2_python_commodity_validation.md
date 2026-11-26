# Week 3 Day 2 - Python Commodity Price Validation

## Objective

Strengthen validation of the Week 3 commodity price dataset before
downstream Snowflake and dbt processing.

## Dataset

File:
data/commodity_prices.csv

Rows:
30

Commodities:
- Avocado
- Banana
- Mango

Markets:
- Hyderabad
- Vijayawada

## Validation Performed

The validation script checks:

1. Required CSV columns.
2. Dataset is not empty.
3. Missing values.
4. Date format.
5. Allowed commodities.
6. Allowed markets.
7. Numeric price values.
8. Positive prices.
9. Duplicate date/commodity/market records.

## Validation Result

Commodity price validation passed.

- Rows: 30
- Date format: YYYY-MM-DD
- Duplicate records: 0
- Missing values: 0
- Price validation: positive numeric values

## Downstream Readiness

The validated dataset is ready for downstream Snowflake/dbt
commodity price and arbitrage analytics processing.

## Week 3 Day 2 Status

Python commodity price validation completed successfully.
