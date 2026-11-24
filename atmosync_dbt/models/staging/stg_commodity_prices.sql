{{ config(
    materialized='view'
) }}

SELECT
    PRICE_DATE,
    COMMODITY,
    MARKET,
    PRICE_PER_KG
FROM {{ ref('commodity_prices') }}
