from statistics import mean, pstdev


def parse_klines(klines):
    candles = []

    for candle in klines:
        candles.append({
            "open_time": candle[0],
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": float(candle[5]),
        })

    return candles


def calculate_returns(closes):
    returns = []

    for previous, current in zip(
        closes,
        closes[1:]
    ):
        if previous == 0:
            continue

        returns.append(
            (current - previous) / previous
        )

    return returns


def analyze(candles):
    if not candles:
        raise ValueError(
            "No candle data available."
        )

    closes = [
        candle["close"]
        for candle in candles
    ]

    highs = [
        candle["high"]
        for candle in candles
    ]

    lows = [
        candle["low"]
        for candle in candles
    ]

    volumes = [
        candle["volume"]
        for candle in candles
    ]

    returns = calculate_returns(closes)

    first_price = closes[0]
    last_price = closes[-1]

    change_percent = (
        (last_price - first_price)
        / first_price
        * 100
    )

    volatility = (
        pstdev(returns) * 100
        if returns
        else 0
    )

    average_price = mean(closes)
    average_volume = mean(volumes)

    return {
        "first_price": first_price,
        "last_price": last_price,
        "highest_price": max(highs),
        "lowest_price": min(lows),
        "average_price": average_price,
        "average_volume": average_volume,
        "change_percent": change_percent,
        "volatility_percent": volatility,
        "candles": len(candles)
    }


def classify_market(change_percent, volatility):
    if volatility >= 3:
        volatility_label = "High volatility"
    elif volatility >= 1:
        volatility_label = "Moderate volatility"
    else:
        volatility_label = "Low volatility"

    if change_percent >= 5:
        trend = "Strong upward movement"
    elif change_percent >= 1:
        trend = "Positive movement"
    elif change_percent <= -5:
        trend = "Strong downward movement"
    elif change_percent <= -1:
        trend = "Negative movement"
    else:
        trend = "Mostly sideways"

    return trend, volatility_label
