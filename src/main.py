from datetime import datetime, timezone

from .api import get_klines
from .analyzer import (
    analyze,
    classify_market,
    parse_klines
)


SYMBOL = "BTCUSDT"
INTERVAL = "1h"
LIMIT = 100


def money(value):
    return f"${value:,.2f}"


def main():
    print("=" * 55)
    print("CRYPTO MARKET ANALYZER")
    print("=" * 55)

    print()
    print(
        f"Asset: {SYMBOL}"
    )

    print(
        f"Interval: {INTERVAL}"
    )

    print(
        f"Candles: {LIMIT}"
    )

    print()
    print("Fetching market data...")

    raw_data = get_klines(
        symbol=SYMBOL,
        interval=INTERVAL,
        limit=LIMIT
    )

    candles = parse_klines(
        raw_data
    )

    result = analyze(
        candles
    )

    trend, volatility_label = classify_market(
        result["change_percent"],
        result["volatility_percent"]
    )

    now = datetime.now(
        timezone.utc
    )

    print()
    print(
        f"Updated: {now.isoformat()}"
    )

    print()
    print("-" * 55)

    print(
        f"First price:      "
        f"{money(result['first_price'])}"
    )

    print(
        f"Latest price:     "
        f"{money(result['last_price'])}"
    )

    print(
        f"Highest price:    "
        f"{money(result['highest_price'])}"
    )

    print(
        f"Lowest price:     "
        f"{money(result['lowest_price'])}"
    )

    print(
        f"Average price:    "
        f"{money(result['average_price'])}"
    )

    print(
        f"Average volume:   "
        f"{result['average_volume']:,.4f}"
    )

    print(
        f"Price change:     "
        f"{result['change_percent']:.2f}%"
    )

    print(
        f"Volatility:       "
        f"{result['volatility_percent']:.2f}%"
    )

    print("-" * 55)

    print(
        f"Trend:            {trend}"
    )

    print(
        f"Volatility level: {volatility_label}"
    )

    print("-" * 55)


if __name__ == "__main__":
    main()
