# CodeAlpha Stock Portfolio Tracker

CodeAlpha Python Programming internship task, by Steven Rios.

## Overview
Enter stock tickers and quantities, and the tracker calculates each holding's value and your total investment from a hardcoded price list (AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA; sample prices, not live data). Unknown tickers and invalid quantities (non-integer, zero or negative) are rejected. Results can optionally be saved to `portfolio.txt` and/or `portfolio.csv`.

## How to run
Requires Python 3.8+.
```bash
python portfolio.py
```
Run the tests:
```bash
python -m unittest -v
```

## Sample output
Captured from a scripted run with piped input (typed answers are not echoed when piped).
```text
=== Stock Portfolio Tracker ===
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA
Enter stock ticker (or 'done'): Quantity of AAPL: Enter stock ticker (or 'done'): Quantity of TSLA: Enter stock ticker (or 'done'): Unknown ticker 'XYZ'. Choose from: AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA
Enter stock ticker (or 'done'): Quantity of MSFT: Quantity must be a whole number greater than 0.
Enter stock ticker (or 'done'): Quantity of NVDA: Enter stock ticker (or 'done'): 
Stock      Qty     Price       Value
------------------------------------
AAPL        10    180.00    1,800.00
TSLA         2    250.00      500.00
NVDA         5    120.00      600.00
------------------------------------
Total investment:           2,900.00

Save results? (txt/csv/both/no):
```

## Concepts used
- Dictionaries for prices and holdings
- Loops, `input()` and validation with `try/except`
- Basic arithmetic and f-string formatting
- File handling: plain text and `csv` module
- `unittest` with mocked input and temp files

## LinkedIn demo script (60-90 s)
1. (0-10s) Intro: "CodeAlpha Task 2: Stock Portfolio Tracker."
2. (10-25s) Show the `STOCK_PRICES` dictionary in `portfolio.py`.
3. (25-55s) Run it: add AAPL 10 and TSLA 2, try `XYZ` and `-1` to show validation, type `done`.
4. (55-75s) Show the table and total, choose `both`, open `portfolio.csv`.
5. (75-90s) Run the tests and thank @CodeAlpha.

## License
MIT, see [LICENSE](LICENSE).
