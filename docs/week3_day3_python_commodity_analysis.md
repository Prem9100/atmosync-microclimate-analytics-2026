# Week 3 Day 3 - Python Commodity Price Analysis

## Objective

Extend the Week 3 commodity price data preparation by creating a reusable Python analysis script that summarizes commodity prices by market.

## Analysis Script

File:

src/atmosync/analyze_commodity_prices.py

The script:

- Reads data/commodity_prices.csv.
- Groups records by commodity and market.
- Calculates the number of records.
- Calculates the average price per kg.
- Identifies the minimum price per kg.
- Identifies the maximum price per kg.
- Prints the summary in a readable format.

## Validation Result

The analysis processed all 30 commodity price records.

### Avocado

- Hyderabad: Average ?185.00/kg
- Vijayawada: Average ?202.80/kg

### Banana

- Hyderabad: Average ?57.40/kg
- Vijayawada: Average ?65.40/kg

### Mango

- Hyderabad: Average ?100.00/kg
- Vijayawada: Average ?116.20/kg

Each commodity contains 5 records for each market.

## Analytics Readiness

The generated market-level price summaries provide a validated input for downstream arbitrage analysis.

The results show a higher average price in Vijayawada than Hyderabad for all three commodities in the current synthetic dataset.

## Status

Week 3 Day 3 Python commodity price analysis completed successfully.
