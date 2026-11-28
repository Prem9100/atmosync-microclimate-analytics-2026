# Week 3 Day 3 - Superset Commodity Price Comparison

## Objective

Prepare the first executable SQL definition for the Week 3 Superset dashboard using the commodity arbitrage analytics dataset.

## SQL Definition

File:

docs/superset/week3_day3_commodity_price_comparison.sql

The query reads from:

ATMOSYNC_DB.RAW.COMMODITY_ARBITRAGE_ANALYTICS

It selects:

- PRICE_DATE
- COMMODITY
- SOURCE_MARKET
- DESTINATION_MARKET
- SOURCE_PRICE_PER_KG
- DESTINATION_PRICE_PER_KG
- PRICE_DIFFERENCE_PER_KG

The results are ordered by price date and commodity.

## Dashboard Purpose

The query provides the data required for a Commodity Price Comparison visualization.

The planned visualization will allow comparison of:

- Source market price
- Destination market price
- Price difference
- Commodity
- Date

## Superset Integration

The SQL definition is prepared for use in Superset SQL Lab or as the query definition for a dashboard dataset.

Live Superset execution is not claimed in this validation because the database connection was not available during the earlier Week 3 dashboard setup.

## Status

Week 3 Day 3 Superset SQL preparation completed successfully.
