import json
from datetime import datetime

stock_data = {}

def add_item(item: str = "default", qty: int = 0, logs=None):
    if logs is None:
        logs = []
    if not item or not isinstance(qty, int):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: {item} not found in stock.")


def get_qty(item: str) -> int:
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}


def save_data(file: str = "inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold: int = 5):
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    add_item("apple", 10)
    add_item("banana", 3)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
