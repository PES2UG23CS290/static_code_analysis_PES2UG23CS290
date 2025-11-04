"""Inventory management system for adding, removing, and saving stock data."""

import json
from datetime import datetime

# Global variable to hold stock items and quantities
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item with a given quantity to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not found; ignore
        pass


def get_qty(item):
    """Return the quantity of a given item, or 0 if it doesn't exist."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        stock_data.clear()


def save_data(file="inventory.json"):
    """Save the current stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """Print the current stock report."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given threshold quantity."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    print("Operation complete.")  # Replaced unsafe eval


if __name__ == "__main__":
    main()
