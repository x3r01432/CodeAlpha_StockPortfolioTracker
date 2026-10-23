"""Stock Portfolio Tracker (CodeAlpha Python Task 2).

Enter stock tickers and quantities; the program totals your investment
using a hardcoded price list and can save the result to .txt or .csv.
"""
import csv

# Hardcoded stock prices in USD (sample values, not live data)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175,
    "NVDA": 120,
}


def parse_quantity(text):
    """Return a positive int, or None if the text is not a valid quantity."""
    try:
        qty = int(text)
    except ValueError:
        return None
    return qty if qty > 0 else None


def calculate_portfolio(holdings):
    """Turn {ticker: qty} into rows (ticker, qty, price, value) and a total."""
    rows = []
    total = 0
    for ticker, qty in holdings.items():
        price = STOCK_PRICES[ticker]
        value = price * qty
        rows.append((ticker, qty, price, value))
        total += value
    return rows, total


def format_report(rows, total):
    """Build a readable text table."""
    lines = [f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}", "-" * 36]
    for ticker, qty, price, value in rows:
        lines.append(f"{ticker:<8}{qty:>6}{price:>10,.2f}{value:>12,.2f}")
    lines.append("-" * 36)
    lines.append(f"{'Total investment:':<24}{total:>12,.2f}")
    return "\n".join(lines)


def save_txt(path, rows, total):
    with open(path, "w", encoding="utf-8") as f:
        f.write(format_report(rows, total) + "\n")


def save_csv(path, rows, total):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])


def collect_holdings():
    """Ask for tickers and quantities until the user types 'done'."""
    holdings = {}
    print("Available stocks:", ", ".join(STOCK_PRICES))
    while True:
        ticker = input("Enter stock ticker (or 'done'): ").strip().upper()
        if ticker == "DONE":
            return holdings
        if ticker not in STOCK_PRICES:
            print(f"Unknown ticker '{ticker}'. Choose from: {', '.join(STOCK_PRICES)}")
            continue
        qty = parse_quantity(input(f"Quantity of {ticker}: ").strip())
        if qty is None:
            print("Quantity must be a whole number greater than 0.")
            continue
        holdings[ticker] = holdings.get(ticker, 0) + qty  # add to existing


def main():
    print("=== Stock Portfolio Tracker ===")
    holdings = collect_holdings()
    if not holdings:
        print("No stocks entered. Goodbye!")
        return
    rows, total = calculate_portfolio(holdings)
    print("\n" + format_report(rows, total))
    choice = input("\nSave results? (txt/csv/both/no): ").strip().lower()
    if choice in ("txt", "both"):
        save_txt("portfolio.txt", rows, total)
        print("Saved portfolio.txt")
    if choice in ("csv", "both"):
        save_csv("portfolio.csv", rows, total)
        print("Saved portfolio.csv")


if __name__ == "__main__":
    main()
