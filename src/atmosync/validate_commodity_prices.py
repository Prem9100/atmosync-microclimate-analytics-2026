import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "commodity_prices.csv"

REQUIRED_COLUMNS = [
    "price_date",
    "commodity",
    "market",
    "price_per_kg",
]

EXPECTED_COMMODITIES = {"Avocado", "Banana", "Mango"}
EXPECTED_MARKETS = {"Hyderabad", "Vijayawada"}


def validate():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if reader.fieldnames != REQUIRED_COLUMNS:
        raise ValueError(
            f"Invalid columns. Expected {REQUIRED_COLUMNS}, "
            f"found {reader.fieldnames}"
        )

    if not rows:
        raise ValueError("Dataset is empty.")

    seen_records = set()

    for row_number, row in enumerate(rows, start=2):
        if any(not row[column].strip() for column in REQUIRED_COLUMNS):
            raise ValueError(f"Missing value found at CSV row {row_number}")

        try:
            datetime.strptime(row["price_date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Invalid date format at row {row_number}: {row['price_date']}"
            )

        commodity = row["commodity"].strip()
        market = row["market"].strip()

        if commodity not in EXPECTED_COMMODITIES:
            raise ValueError(
                f"Unexpected commodity at row {row_number}: {commodity}"
            )

        if market not in EXPECTED_MARKETS:
            raise ValueError(
                f"Unexpected market at row {row_number}: {market}"
            )

        try:
            price = float(row["price_per_kg"])
        except ValueError:
            raise ValueError(
                f"Invalid price at row {row_number}: {row['price_per_kg']}"
            )

        if price <= 0:
            raise ValueError(
                f"Price must be greater than zero at row {row_number}"
            )

        record_key = (
            row["price_date"],
            commodity,
            market,
        )

        if record_key in seen_records:
            raise ValueError(
                f"Duplicate date/commodity/market record at row {row_number}"
            )

        seen_records.add(record_key)

    print("Commodity price validation passed.")
    print(f"Rows: {len(rows)}")
    print(f"Commodities: {sorted(EXPECTED_COMMODITIES)}")
    print(f"Markets: {sorted(EXPECTED_MARKETS)}")
    print("Date format: YYYY-MM-DD")
    print("Duplicate records: 0")
    print("Missing values: 0")
    print("Price validation: positive numeric values")


if __name__ == "__main__":
    validate()
