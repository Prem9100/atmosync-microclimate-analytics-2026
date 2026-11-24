import csv
from pathlib import Path

DATA_FILE = Path("data/commodity_prices.csv")

REQUIRED_COLUMNS = {
    "price_date",
    "commodity",
    "market",
    "price_per_kg",
}

def validate_commodity_prices():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing file: {DATA_FILE}")

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        raise ValueError("Commodity price dataset is empty.")

    actual_columns = set(rows[0].keys())

    if actual_columns != REQUIRED_COLUMNS:
        raise ValueError(
            f"Invalid columns. Expected {REQUIRED_COLUMNS}, got {actual_columns}"
        )

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if not row[column].strip():
                raise ValueError(
                    f"Missing value in column '{column}' at CSV row {row_number}"
                )

        try:
            price = float(row["price_per_kg"])
        except ValueError:
            raise ValueError(
                f"Invalid price at CSV row {row_number}: {row['price_per_kg']}"
            )

        if price <= 0:
            raise ValueError(
                f"Price must be greater than zero at CSV row {row_number}"
            )

    commodities = sorted({row["commodity"] for row in rows})
    markets = sorted({row["market"] for row in rows})

    print("Commodity price validation passed.")
    print(f"Rows: {len(rows)}")
    print(f"Commodities: {commodities}")
    print(f"Markets: {markets}")


if __name__ == "__main__":
    validate_commodity_prices()
