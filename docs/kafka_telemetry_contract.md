# AtmoSync Kafka Telemetry Contract

## 1. Purpose

This document defines the telemetry message format used by the AtmoSync
micro-climate analytics pipeline.

The Python simulator generates synthetic sensor events and the Kafka producer
publishes these events to the Kafka topic:

`atmosync.sensor.telemetry`

The telemetry is consumed downstream for Snowflake ingestion and analytics.

---

## 2. Kafka Configuration

| Property | Value |
|---|---|
| Bootstrap Server | `localhost:9092` |
| Topic | `atmosync.sensor.telemetry` |
| Message Key | `container_id` |
| Message Value | JSON |
| Producer | `src/atmosync/producer.py` |
| Event Generator | `src/atmosync/simulator.py` |

---

## 3. Telemetry Message Schema

Each Kafka message contains the following JSON fields:

| Field | Type | Description |
|---|---|---|
| `event_id` | String | Unique identifier for the telemetry event |
| `event_ts` | String | UTC timestamp when the event was generated |
| `container_id` | String | Identifier of the shipping container |
| `commodity` | String | Commodity being transported |
| `temperature_c` | Number | Temperature measurement in Celsius |
| `humidity_pct` | Number | Relative humidity percentage |
| `vibration_g` | Number | Vibration measurement |
| `quantity_kg` | Number | Quantity of commodity in kilograms |

---

## 4. Example Event

```json
{
  "event_id": "8e1c7a2e-5a1f-4f32-9f12-7d3c8e4a91b2",
  "event_ts": "2026-11-10T16:30:00+00:00",
  "container_id": "CONT_001",
  "commodity": "Avocado",
  "temperature_c": 6.42,
  "humidity_pct": 82.15,
  "vibration_g": 0.74,
  "quantity_kg": 1250.50
}
---

## 5. Producer Flow

Python Simulator
      |
      v
generate_event()
      |
      v
JSON serialization
      |
      v
Kafka Producer
      |
      v
atmosync.sensor.telemetry

The Kafka message key is the `container_id`.

The event object is serialized to JSON before being published.

---

## 6. Data Flow to Analytics

Python Simulator
       |
       v
Kafka Producer
       |
       v
atmosync.sensor.telemetry
       |
       v
Snowflake Consumer
       |
       v
Snowflake RAW.SENSOR_EVENTS
       |
       v
dbt transformations
       |
       v
Analytics
       |
       v
Apache Superset Dashboard

---

## 7. Synthetic Data Behavior

The simulator generates synthetic demonstration data.

Normal sensor values are generated approximately within:

- Temperature: 4–8 °C
- Humidity: 75–90 %
- Vibration: 0.1–2.0 g

Approximately 15% of generated events simulate abnormal conditions with
higher temperature, humidity, and vibration values.

These values are for project demonstration and analytics testing only.
They are not real commodity quality or safety limits.

---

## 8. Consumer Compatibility

Downstream consumers should use the field names defined in this contract.

The following fields are required for the current telemetry pipeline:

- `event_id`
- `event_ts`
- `container_id`
- `commodity`
- `temperature_c`
- `humidity_pct`
- `vibration_g`
- `quantity_kg`

Changes to field names or data types should be coordinated between the
producer, Kafka consumer, Snowflake schema, dbt models, and dashboard.

---

## 9. Ownership

| Component | Responsibility |
|---|---|
| Python Simulator | Generate synthetic telemetry |
| Kafka Producer | Serialize and publish events |
| Kafka | Transport telemetry messages |
| Snowflake Consumer | Consume and load telemetry |
| Snowflake/dbt | Store and transform telemetry |
| Superset | Visualize analytics |
| Team Lead | Coordinate integration and schema compatibility |
