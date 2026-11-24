# Week 3 Day 1 - Commodity Price Data Preparation

## Objective

Prepare a commodity price dataset for the AtmoSync arbitrage analytics workflow.

## Dataset

File:
data/commodity_prices.csv

Columns:
- price_date
- commodity
- market
- price_per_kg

## Coverage

- Commodities: Avocado, Banana, Mango
- Markets: Hyderabad, Vijayawada
- Dates: 2026-11-20 to 2026-11-24
- Records: 30

## Validation

Validation script:
src/atmosync/validate_commodity_prices.py

Validation result:
- Dataset exists
- Required columns are present
- 30 records loaded successfully
- No missing values
- All prices are greater than zero
- All expected commodities are present
- Both markets are present

## Data Purpose

The dataset will be used in Week 3 to combine commodity prices with sensor telemetry and support:

Sensor Risk + Commodity Price Difference -> Arbitrage Opportunity Analysis

## Note

The current commodity prices are synthetic project data prepared for development and analytics testing.
