import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "atmosync.sensor.telemetry"
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "atmosync-snowflake-consumer")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PRIVATE_KEY_PATH = os.getenv(
    "SNOWFLAKE_PRIVATE_KEY_PATH",
    str(Path(__file__).resolve().parents[2] / "kafka_private_key.pem")
)
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE", "ATMOSYNC_WH")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "ATMOSYNC_DB")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "RAW")
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE", "ATMOSYNC_KAFKA_ROLE")
SIMULATOR_INTERVAL_SECONDS = float(os.getenv("SIMULATOR_INTERVAL_SECONDS", "2"))
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "atmosync.sensor.telemetry"