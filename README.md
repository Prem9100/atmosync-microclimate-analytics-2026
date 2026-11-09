# AtmoSync — Week 1 Starter
Infotact Solutions | Data Analytics | Ref: ITS/DA/1606

This starter implements the assigned Week 1 flow:
Python IoT telemetry simulator → Apache Kafka → Snowflake raw table → Apache Superset.

## Prerequisites (Windows)
- Python 3.11+ (Snowflake Connector for Python supports Windows on Python 3.11+)
- Git for Windows
- Docker Desktop with WSL 2 backend
- VS Code

## Setup
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
Copy-Item config\.env.example .env
```
Edit `.env` with your Snowflake account details. Never commit `.env`. The package is installed in editable mode so `python -m atmosync...` works from the repository root.

If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Start Kafka and Superset
```powershell
docker compose up -d --build
docker compose ps
```
Kafka: `localhost:9092`; Superset: `http://localhost:8088`.

Initialize Superset:
```powershell
docker compose exec superset superset db upgrade
docker compose exec superset superset fab create-admin --username admin --firstname Atmo --lastname Sync --email admin@example.com --password ChangeThisPassword123!
docker compose exec superset superset init
```
Change the sample password. This is for local development only.

Create Kafka topic:
```powershell
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --if-not-exists --topic atmosync.sensor.telemetry --partitions 3 --replication-factor 1
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic atmosync.sensor.telemetry
```

## Snowflake
1. Create a Snowflake account using the account identifier and region shown by Snowflake.
2. Open a SQL worksheet and run `config/snowflake_setup.sql`.
3. Put the account identifier, username and password in `.env` (or use your organization's approved key-pair authentication).
4. Keep credentials private.

## Run the pipeline (three PowerShell terminals)
Activate `.venv` in each terminal.

Terminal 1:
```powershell
python -m atmosync.producer
```
Terminal 2:
```powershell
python -m atmosync.snowflake_consumer
```
Terminal 3 is not needed: the producer itself generates telemetry continuously. Stop it with Ctrl+C.

Verify in Snowflake:
```sql
SELECT COUNT(*) FROM ATMOSYNC_DB.RAW.SENSOR_EVENTS;
SELECT CONTAINER_ID, COUNT(*) AS READINGS,
       ROUND(AVG(TEMPERATURE_C), 2) AS AVG_TEMP_C,
       ROUND(MAX(TEMPERATURE_C), 2) AS MAX_TEMP_C
FROM ATMOSYNC_DB.RAW.SENSOR_EVENTS
GROUP BY CONTAINER_ID ORDER BY MAX_TEMP_C DESC;
```

## Superset
Sign in at `http://localhost:8088`. Add a Snowflake database connection using the Snowflake SQLAlchemy URI documented by Snowflake, then add `ATMOSYNC_DB.RAW.SENSOR_EVENTS` as a dataset. The supplied Superset image installs `snowflake-sqlalchemy`.

## Team of four — suggested split
1. Team lead/integration: repository, Kafka topic, integration and pull requests.
2. Simulator: event schema, Python generator and data validation.
3. Snowflake: database/table setup, consumer and verification SQL.
4. Superset: local deployment, Snowflake connection, dataset and initial charts.

All four members should understand the end-to-end architecture and contribute meaningful work to their own GitHub branches. Confirm actual names and responsibilities with your team.

## Important limitations
The readings and anomaly injection are synthetic test data, not validated food-storage thresholds. Do not use them for real shipment decisions. The first consumer uses row-by-row inserts for a learning-scale pipeline; a production/high-throughput implementation should use Snowpipe Streaming or staged files with COPY INTO. Kafka-to-Snowflake processing is at-least-once, so duplicate event IDs must be handled in later dbt models.
