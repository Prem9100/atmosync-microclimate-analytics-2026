# Week 3 Day 2 - Superset Dashboard Dataset and Chart Definitions

## Objective

Define the Superset dashboard datasets and visualizations required for
Week 3 commodity price and arbitrage analytics.

## Primary Dataset

The planned dashboard dataset is:

ATMOSYNC_DB.RAW.COMMODITY_ARBITRAGE_ANALYTICS

## Required Dashboard Fields

- PRICE_DATE
- COMMODITY
- SOURCE_MARKET
- DESTINATION_MARKET
- SOURCE_PRICE_PER_KG
- DESTINATION_PRICE_PER_KG
- PRICE_DIFFERENCE_PER_KG
- QUANTITY_KG
- AVG_RISK_SCORE
- RISK_LEVEL
- ARBITRAGE_STATUS

## Planned Visualizations

### 1. Commodity Price Comparison

Compare source and destination prices for each commodity.

Dimension:
- COMMODITY

Measures:
- SOURCE_PRICE_PER_KG
- DESTINATION_PRICE_PER_KG

### 2. Price Difference by Commodity

Show the price difference between the source and destination markets.

Dimension:
- COMMODITY

Measure:
- PRICE_DIFFERENCE_PER_KG

### 3. Arbitrage Opportunity Status

Show the number of records for each arbitrage status.

Dimension:
- ARBITRAGE_STATUS

Expected statuses:
- OPPORTUNITY
- HIGH_RISK
- NO_OPPORTUNITY
- NO_SENSOR_DATA

### 4. Risk Level Distribution

Show the distribution of sensor risk levels associated with the analytics data.

Dimension:
- RISK_LEVEL

Measure:
- Record count

### 5. Quantity Available by Commodity

Show the available shipment quantity for each commodity.

Dimension:
- COMMODITY

Measure:
- QUANTITY_KG

### 6. Price Trend

Show source and destination price changes over time.

Time dimension:
- PRICE_DATE

Measures:
- SOURCE_PRICE_PER_KG
- DESTINATION_PRICE_PER_KG

## Dashboard Filters

Planned filters:

- Date
- Commodity
- Source Market
- Destination Market
- Arbitrage Status
- Risk Level

## Week 3 Day 2 Status

Dashboard dataset and visualization requirements have been defined.
Actual Superset chart creation will be completed after the
commodity arbitrage analytics dataset is available and the
Superset database connection is validated.
