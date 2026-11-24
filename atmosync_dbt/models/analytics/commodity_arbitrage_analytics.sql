{{ config(
    materialized='table'
) }}

WITH price_data AS (

    SELECT
        PRICE_DATE,
        COMMODITY,

        MAX(CASE
            WHEN MARKET = 'Hyderabad'
            THEN PRICE_PER_KG
        END) AS SOURCE_PRICE_PER_KG,

        MAX(CASE
            WHEN MARKET = 'Vijayawada'
            THEN PRICE_PER_KG
        END) AS DESTINATION_PRICE_PER_KG

    FROM {{ ref('stg_commodity_prices') }}

    GROUP BY
        PRICE_DATE,
        COMMODITY

),

sensor_data AS (

    SELECT
        CAST(EVENT_TS AS DATE) AS EVENT_DATE,
        COMMODITY,
        SUM(QUANTITY_KG) AS QUANTITY_KG,
        AVG(RISK_SCORE) AS AVG_RISK_SCORE,
        MAX(RISK_LEVEL) AS RISK_LEVEL

    FROM {{ ref('sensor_events_analytics') }}

    GROUP BY
        CAST(EVENT_TS AS DATE),
        COMMODITY

)

SELECT
    p.PRICE_DATE,
    p.COMMODITY,

    'Hyderabad' AS SOURCE_MARKET,
    'Vijayawada' AS DESTINATION_MARKET,

    p.SOURCE_PRICE_PER_KG,
    p.DESTINATION_PRICE_PER_KG,

    p.DESTINATION_PRICE_PER_KG
        - p.SOURCE_PRICE_PER_KG
        AS PRICE_DIFFERENCE_PER_KG,

    s.QUANTITY_KG,
    s.AVG_RISK_SCORE,
    s.RISK_LEVEL,

    CASE
        WHEN s.EVENT_DATE IS NULL
        THEN 'NO_SENSOR_DATA'

        WHEN p.DESTINATION_PRICE_PER_KG
             > p.SOURCE_PRICE_PER_KG
         AND COALESCE(s.AVG_RISK_SCORE, 0) <= 1
        THEN 'OPPORTUNITY'

        WHEN p.DESTINATION_PRICE_PER_KG
             > p.SOURCE_PRICE_PER_KG
         AND COALESCE(s.AVG_RISK_SCORE, 0) > 1
        THEN 'HIGH_RISK'

        ELSE 'NO_OPPORTUNITY'
    END AS ARBITRAGE_STATUS

FROM price_data p

LEFT JOIN sensor_data s
    ON p.PRICE_DATE = s.EVENT_DATE
   AND p.COMMODITY = s.COMMODITY
