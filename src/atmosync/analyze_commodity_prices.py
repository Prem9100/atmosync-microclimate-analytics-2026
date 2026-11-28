import csv
from collections import defaultdict
from pathlib import Path


DATA_FILE = Path("data/commodity_prices.csv")


def load_prices():
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def summarize_prices(rows):
    summary = defaultdict(list)

    for row in rows:
        key = (row["commodity"], row["market"])
        summary[key].append(float(row["price_per_kg"]))

    results = []

    for (commodity, market), prices in sorted(summary.items()):
        results.append({
            "commodity": commodity,
            "market": market,
            "records": len(prices),
            "average_price_per_kg": round(sum(prices) / len(prices), 2),
            "minimum_price_per_kg": round(min(prices), 2),
            "maximum_price_per_kg": round(max(prices), 2),
        })

    return results


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    rows = load_prices()

    if not rows:
        raise ValueError("Commodity price dataset is empty")

    summary = summarize_prices(rows)

    print("Commodity Price Summary")
    print("-" * 70)

    for item in summary:
        print(
            f"{item['commodity']:10} | "
            f"{item['market']:12} | "
            f"Records: {item['records']:2} | "
            f"Avg: {item['average_price_per_kg']:6.2f} | "
            f"Min: {item['minimum_price_per_kg']:6.2f} | "
            f"Max: {item['maximum_price_per_kg']:6.2f}"
        )


if __name__ == "__main__":
    main()
