import random
import time
import uuid
import json
from datetime import datetime, timezone

CONTAINERS = ["CONT_001", "CONT_002", "CONT_003", "CONT_004"]
COMMODITIES = ["Avocado", "Mango", "Banana"]

def generate_event():
    # Synthetic demonstration values only; not real commodity quality limits.
    temp = round(random.uniform(4, 8), 2)
    humidity = round(random.uniform(75, 90), 2)
    vibration = round(random.uniform(0.1, 2.0), 2)
    if random.random() < 0.15:
        temp = round(random.uniform(10, 16), 2)
        humidity = round(random.uniform(90, 98), 2)
        vibration = round(random.uniform(2.5, 5.0), 2)
    return {
        "event_id": str(uuid.uuid4()),
        "event_ts": datetime.now(timezone.utc).isoformat(),
        "container_id": random.choice(CONTAINERS),
        "commodity": random.choice(COMMODITIES),
        "temperature_c": temp,
        "humidity_pct": humidity,
        "vibration_g": vibration,
        "quantity_kg": round(random.uniform(500, 2000), 2),
    }
