import random
from datetime import datetime, timezone


def generate_sensor_data():
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    vibration = round(random.uniform(0.1, 1.0), 3)

    return {
        "event_id": f"evt-{random.randint(100000, 999999)}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": temperature,
        "humidity_pct": humidity,
        "vibration_g": vibration
    }