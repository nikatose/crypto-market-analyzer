import json
import urllib.parse
import urllib.request


BINANCE_API = "https://api.binance.com/api/v3/klines"


def get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=100
):
    params = urllib.parse.urlencode({
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    })

    url = f"{BINANCE_API}?{params}"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "crypto-market-analyzer"
        }
    )

    with urllib.request.urlopen(
        request,
        timeout=15
    ) as response:

        return json.loads(
            response.read().decode("utf-8")
        )
