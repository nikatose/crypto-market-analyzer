import unittest

from src.analyzer import (
    analyze,
    calculate_returns,
    classify_market
)


class AnalyzerTests(unittest.TestCase):

    def test_returns(self):
        values = [
            100,
            110,
            121
        ]

        returns = calculate_returns(
            values
        )

        self.assertAlmostEqual(
            returns[0],
            0.10
        )

        self.assertAlmostEqual(
            returns[1],
            0.10
        )


    def test_analysis(self):

        candles = [
            {
                "open_time": 1,
                "open": 100,
                "high": 110,
                "low": 90,
                "close": 105,
                "volume": 10
            },
            {
                "open_time": 2,
                "open": 105,
                "high": 120,
                "low": 100,
                "close": 115,
                "volume": 20
            }
        ]

        result = analyze(
            candles
        )

        self.assertEqual(
            result["first_price"],
            105
        )

        self.assertEqual(
            result["last_price"],
            115
        )

        self.assertEqual(
            result["highest_price"],
            120
        )

        self.assertEqual(
            result["lowest_price"],
            90
        )


    def test_market_classification(self):

        trend, volatility = classify_market(
            6,
            2
        )

        self.assertEqual(
            trend,
            "Strong upward movement"
        )

        self.assertEqual(
            volatility,
            "Moderate volatility"
        )


if __name__ == "__main__":
    unittest.main()
