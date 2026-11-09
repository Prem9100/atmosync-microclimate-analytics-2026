from src.atmosync.simulator import generate_event


def test_generate_event_contains_required_fields():
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


def test_generate_event_has_valid_sensor_values():
    event = generate_event()

    assert isinstance(event["event_id"], str)
    assert isinstance(event["event_ts"], str)

    assert isinstance(event["temperature_c"], (int, float))
    assert isinstance(event["humidity_pct"], (int, float))
    assert isinstance(event["vibration_g"], (int, float))
    assert isinstance(event["quantity_kg"], (int, float))


def test_generate_event_has_container_and_commodity():
    event = generate_event()

    assert event["container_id"]
    assert event["commodity"]