from datetime import datetime
from uuid import UUID

from src.atmosync.simulator import generate_event


def test_generate_event_has_required_fields():
    event = generate_event()

    required_fields = {
        "event_id",
        "event_ts",
        "container_id",
        "commodity",
        "temperature_c",
        "humidity_pct",
        "vibration_g",
        "quantity_kg",
    }

    assert required_fields.issubset(event.keys())


def test_generate_event_has_correct_types():
    event = generate_event()

    assert isinstance(event["event_id"], str)
    assert isinstance(event["event_ts"], str)
    assert isinstance(event["container_id"], str)
    assert isinstance(event["commodity"], str)
    assert isinstance(event["temperature_c"], float)
    assert isinstance(event["humidity_pct"], float)
    assert isinstance(event["vibration_g"], float)
    assert isinstance(event["quantity_kg"], float)


def test_generate_event_has_container_and_commodity():
    event = generate_event()

    assert event["container_id"]
    assert event["commodity"]


def test_generate_event_has_valid_ranges():
    event = generate_event()

    assert 4.0 <= event["temperature_c"] <= 16.0
    assert 75.0 <= event["humidity_pct"] <= 98.0
    assert 0.1 <= event["vibration_g"] <= 5.0
    assert 500.0 <= event["quantity_kg"] <= 2000.0


def test_generate_event_has_valid_uuid():
    event = generate_event()

    UUID(event["event_id"])


def test_generate_event_has_valid_timestamp():
    event = generate_event()

    timestamp = datetime.fromisoformat(event["event_ts"])

    assert timestamp.tzinfo is not None