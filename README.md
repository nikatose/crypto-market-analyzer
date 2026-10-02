# Crypto Market Analyzer

A lightweight Python tool for analyzing cryptocurrency market data.

The project fetches public OHLCV market data and calculates basic market statistics such as price change, average price, trading range and return volatility.

## Features

- Python-based market analysis
- Public market data API
- OHLCV candle processing
- Price statistics
- Return calculation
- Volatility calculation
- Market movement classification
- Unit tests
- GitHub Actions
- Zero third-party runtime dependencies

## Market Summary

The analyzer provides a compact overview of recent market conditions including:

- Price movement
- Trading range
- Average price
- Trading volume
- Return volatility
- Market movement classification

## Project Structure

```text
crypto-market-analyzer
│
├── .github/
│   └── workflows/
│       └── analyze.yml
│
├── data/
│
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── analyzer.py
│   └── main.py
│
├── tests/
│   └── test_analyzer.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
