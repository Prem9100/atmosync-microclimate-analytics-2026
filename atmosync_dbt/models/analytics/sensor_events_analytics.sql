{{ config(
    materialized='table'
) }}

SELECT
    EVENT_ID,
    EVENT_TS,
    CONTAINER_ID,
    COMMODITY,
    TEMPERATURE_C,
    HUMIDITY_PCT,
    VIBRATION_G,
    QUANTITY_KG,

    CASE
        WHEN TEMPERATURE_C > 8 THEN 'HIGH'
        WHEN TEMPERATURE_C < 4 THEN 'LOW'
        ELSE 'NORMAL'
    END AS TEMPERATURE_STATUS,

    CASE
        WHEN HUMIDITY_PCT > 90 THEN 'HIGH'
        WHEN HUMIDITY_PCT < 75 THEN 'LOW'
        ELSE 'NORMAL'
    END AS HUMIDITY_STATUS,

    CASE
        WHEN VIBRATION_G > 2 THEN 'HIGH'
        ELSE 'NORMAL'
    END AS VIBRATION_STATUS,

    CASE
        WHEN TEMPERATURE_C > 8
          OR HUMIDITY_PCT > 90
          OR VIBRATION_G > 2
        THEN 'ALERT'
        ELSE 'NORMAL'
    END AS OVERALL_STATUS,

    (
        CASE
            WHEN TEMPERATURE_C > 8 OR TEMPERATURE_C < 4 THEN 1
            ELSE 0
        END
        +
        CASE
            WHEN HUMIDITY_PCT > 90 OR HUMIDITY_PCT < 75 THEN 1
            ELSE 0
        END
        +
        CASE
            WHEN VIBRATION_G > 2 THEN 1
            ELSE 0
        END
    ) AS RISK_SCORE,

    CASE
        WHEN (
            CASE
                WHEN TEMPERATURE_C > 8 OR TEMPERATURE_C < 4 THEN 1
                ELSE 0
            END
            +
            CASE
                WHEN HUMIDITY_PCT > 90 OR HUMIDITY_PCT < 75 THEN 1
                ELSE 0
            END
            +
            CASE
                WHEN VIBRATION_G > 2 THEN 1
                ELSE 0
            END
        ) = 0 THEN 'LOW'

        WHEN (
            CASE
                WHEN TEMPERATURE_C > 8 OR TEMPERATURE_C < 4 THEN 1
                ELSE 0
            END
            +
            CASE
                WHEN HUMIDITY_PCT > 90 OR HUMIDITY_PCT < 75 THEN 1
                ELSE 0
            END
            +
            CASE
                WHEN VIBRATION_G > 2 THEN 1
                ELSE 0
            END
        ) = 1 THEN 'MEDIUM'

        ELSE 'HIGH'
    END AS RISK_LEVEL

FROM {{ ref('stg_sensor_events') }}