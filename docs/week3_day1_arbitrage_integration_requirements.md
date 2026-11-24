# Week 3 Day 1 - Arbitrage Integration Requirements

## Objective

Define the integration requirements for combining sensor telemetry with commodity price data.

## Current Inputs

### Sensor Telemetry

Existing dbt analytics model:
atmosync_dbt/models/analytics/sensor_events_analytics.sql

Existing sensor fields include:
- EVENT_ID
- EVENT_TS
- CONTAINER_ID
- COMMODITY
- TEMPERATURE_C
- HUMIDITY_PCT
- VIBRATION_G
- QUANTITY_KG
- RISK_SCORE
- RISK_LEVEL
- OVERALL_STATUS

### Commodity Price Data

Source:
data/commodity_prices.csv

Fields:
- price_date
- commodity
- market
- price_per_kg

Current commodities:
- Avocado
- Banana
- Mango

Current markets:
- Hyderabad
- Vijayawada

## Week 3 Analytics Requirement

Member 3 should design a dbt model that can combine:

Sensor Telemetry
+
Commodity Prices
=
Arbitrage Analytics

The model should support analysis of:

1. Commodity price differences between markets.
2. Potential price advantage between the source and destination markets.
3. Sensor risk associated with the commodity.
4. Quantity available for the shipment.
5. Potential arbitrage opportunity after considering risk.

## Integration Direction

The initial analytical relationship should be based on:

- commodity
- date
- market

The sensor event timestamp should be converted to a comparable date where required.

## Expected Future Output

The analytical model should eventually provide fields such as:

- commodity
- price_date
- source_market
- destination_market
- source_price_per_kg
- destination_price_per_kg
- price_difference_per_kg
- quantity_kg
- risk_score
- risk_level
- arbitrage_status

## Important

Do not modify the existing sensor analytics model until the commodity-price integration design is reviewed.

Member 3 should create a separate Week 3 model for the initial arbitrage analysis.

## Team Lead Review

Member 2 commodity-price data has been validated and merged into main.

Next dependency:
Member 3 -> Snowflake/dbt commodity price and arbitrage model.
