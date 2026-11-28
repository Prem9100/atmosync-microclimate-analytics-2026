SELECT *
FROM {{ ref('commodity_arbitrage_analytics') }}
WHERE ARBITRAGE_STATUS NOT IN (
    'OPPORTUNITY',
    'HIGH_RISK',
    'NO_OPPORTUNITY',
    'NO_SENSOR_DATA'
)
