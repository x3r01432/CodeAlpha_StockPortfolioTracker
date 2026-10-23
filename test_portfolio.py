import csv
import io
import os
import tempfile
import unittest
from unittest.mock import patch

import portfolio


class PortfolioTests(unittest.TestCase):
    def test_parse_quantity(self):
        self.assertEqual(portfolio.parse_quantity("5"), 5)
        for bad in ["0", "-3", "2.5", "abc", ""]:
            self.assertIsNone(portfolio.parse_quantity(bad))

    def test_calculate(self):
        rows, total = portfolio.calculate_portfolio({"AAPL": 10, "TSLA": 2})
        self.assertEqual(total, 180 * 10 + 250 * 2)
        self.assertEqual(rows[0], ("AAPL", 10, 180, 1800))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_collect_validates(self, out):
        inputs = ["xyz", "aapl", "-1", "aapl", "two", "AAPL", "3", "aapl", "2", "done"]
        with patch("builtins.input", side_effect=inputs):
            self.assertEqual(portfolio.collect_holdings(), {"AAPL": 5})
        self.assertIn("Unknown ticker", out.getvalue())

    def test_save_files(self):
        rows, total = portfolio.calculate_portfolio({"MSFT": 1})
        with tempfile.TemporaryDirectory() as d:
            t, c = os.path.join(d, "p.txt"), os.path.join(d, "p.csv")
            portfolio.save_txt(t, rows, total)
            portfolio.save_csv(c, rows, total)
            self.assertIn("410.00", open(t).read())
            data = list(csv.reader(open(c)))
            self.assertEqual(data[0], ["Stock", "Quantity", "Price", "Value"])
            self.assertEqual(data[-1][0], "TOTAL")


if __name__ == "__main__":
    unittest.main()
