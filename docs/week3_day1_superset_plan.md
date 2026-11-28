# Week 3 Day 1 - Superset Dashboard Plan

## Project
AtmoSync: Micro-Climate Arbitrage Analytics

## Week 3 Objective
Prepare the Superset dashboard requirements for commodity price and arbitrage analytics.

## Planned Dashboard Analytics

### Commodity Price Analysis
- Compare Hyderabad and Vijayawada prices.
- Show price difference per kg.
- Analyze price differences by commodity and date.

### Arbitrage Analysis
- Display potential arbitrage opportunities.
- Show source and destination markets.
- Display arbitrage status.

### Sensor Risk Integration
- Display quantity and sensor risk when matching telemetry is available.
- Clearly identify records with `NO_SENSOR_DATA`.
- Do not treat missing sensor data as zero risk.

## Planned Visualizations

1. Commodity price comparison.
2. Price difference by commodity.
3. Arbitrage status distribution.
4. Commodity-wise arbitrage table.
5. Sensor risk and quantity information when available.

## Data Source

Week 3 analytics model:

`ATMOSYNC_DB.RAW.COMMODITY_ARBITRAGE_ANALYTICS`

The dashboard will be connected to this model after the Snowflake/Superset database connection is available.

## Current Status

The Week 3 dashboard requirements are documented.
Dashboard implementation will be completed after the Superset database connection is configured.
