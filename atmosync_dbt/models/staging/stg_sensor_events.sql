{{ config(
    materialized='view'
) }}

SELECT
    EVENT_ID,
    EVENT_TS,
    CONTAINER_ID,
    COMMODITY,
    TEMPERATURE_C,
    HUMIDITY_PCT,
    VIBRATION_G,
    QUANTITY_KG
FROM {{ source('raw', 'SENSOR_EVENTS') }}