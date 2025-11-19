import json
import csv
from typing import Dict, Any, Tuple


def export_order(order: Dict[str, Any], json_path: str, csv_path: str) -> Tuple[str, str]:
    """
    - Write the whole order dict to JSON (pretty indentation).
    - Write a CSV with: sku, name, qty, unit_price, line_total.
    - Return (json_path, csv_path).
    - Raise IO errors normally.
    """

    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(order, jf, indent=2)

    catalog = order["catalog"]
    cart = order["cart"]

    with open(csv_path, "w", newline="", encoding="utf-8") as cf:
        writer = csv.writer(cf)

        writer.writerow(["sku", "name", "qty", "unit_price", "line_total"])

        for item in cart:
            sku = item["sku"]
            qty = item["qty"]
            product = catalog[sku]

            name = product["name"]
            unit_price = product["price"]
            line_total = round(unit_price * qty, 2)

            writer.writerow([sku, name, qty, unit_price, line_total])

    return json_path, csv_path
