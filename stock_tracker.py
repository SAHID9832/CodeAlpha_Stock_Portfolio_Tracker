"""
Stock Portfolio Tracker
-----------------------
Goal:
Calculate total investment using manually defined stock prices.

Concepts Used:
- Dictionary
- User Input / Output
- Basic Arithmetic
- File Handling (CSV / TXT)

Author: Sahid
"""

from datetime import datetime
import csv

# -------------------------------------------------
# Hardcoded Stock Prices (Manual Input Only)
# -------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# -------------------------------------------------
# Utility Functions
# -------------------------------------------------
def display_title():
    print("\n" + "=" * 50)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 50)


def get_integer_input(message):
    """Safely read integer input."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")


def get_portfolio_data():
    """Collect stock details from the user."""
    portfolio = []
    total_value = 0

    count = get_integer_input("Enter number of stocks: ")

    for i in range(1, count + 1):
        print(f"\nStock {i}")
        stock_name = input("Enter stock name: ").upper()
        quantity = get_integer_input("Enter quantity: ")

        if stock_name not in STOCK_PRICES:
            print("⚠️ Stock not found. Skipped.")
            continue

        price = STOCK_PRICES[stock_name]
        investment = price * quantity
        total_value += investment

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "value": investment
        })

    return portfolio, total_value


def display_portfolio(portfolio, total):
    """Display investment summary."""
    print("\n📊 PORTFOLIO SUMMARY")
    print("-" * 50)

    for item in portfolio:
        print(
            f"{item['stock']:<6} | "
            f"Qty: {item['quantity']:<3} | "
            f"Price: ₹{item['price']:<4} | "
            f"Value: ₹{item['value']}"
        )

    print("-" * 50)
    print(f"💰 Total Investment Value: ₹{total}")


def save_to_csv(portfolio, total):
    """Save portfolio data to CSV."""
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment Value"]
        )
        for item in portfolio:
            writer.writerow(
                [item["stock"], item["quantity"], item["price"], item["value"]]
            )
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])


def save_to_txt(portfolio, total):
    """Save portfolio data to TXT."""
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("-" * 40 + "\n")

        for item in portfolio:
            file.write(
                f"{item['stock']} | Qty: {item['quantity']} | "
                f"Price: ₹{item['price']} | Value: ₹{item['value']}\n"
            )

        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ₹{total}\n")
        file.write(f"Generated On: {datetime.now()}\n")


# -------------------------------------------------
# Main Program
# -------------------------------------------------
def main():
    display_title()

    portfolio, total = get_portfolio_data()
    display_portfolio(portfolio, total)

    choice = input(
        "\nDo you want to save the result? (csv / txt / no): "
    ).lower()

    if choice == "csv":
        save_to_csv(portfolio, total)
        print("✅ Data saved to portfolio.csv")

    elif choice == "txt":
        save_to_txt(portfolio, total)
        print("✅ Data saved to portfolio.txt")

    else:
        print("ℹ️ Data not saved.")

    print("\n✔ Program completed successfully.")


if __name__ == "__main__":
    main()
