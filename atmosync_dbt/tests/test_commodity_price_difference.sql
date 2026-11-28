SELECT *
FROM {{ ref('commodity_arbitrage_analytics') }}
WHERE PRICE_DIFFERENCE_PER_KG != (
    DESTINATION_PRICE_PER_KG - SOURCE_PRICE_PER_KG
)
