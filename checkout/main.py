"""
Mini E-Commerce Order Processor
Main entry point for the checkout pipeline.
"""

from checkout.src.pipeline import process_order
from checkout.src.team9_receipt import generate_receipt
from checkout.src.team10_export import export_order


def main():
    # === Sample Data (from the project PDF) ===
    catalog_data = [
        {"sku": "B100", "name": "Intro to Python", "price": 50.0, "tax_code": "STD", "weight": 0.6, "category": "BOOKS"},
        {"sku": "G200", "name": "Gaming Mouse", "price": 80.0, "tax_code": "LUX", "weight": 0.2, "category": "GADGETS"},
        {"sku": "A300", "name": "Alkaline Batteries (4pk)", "price": 12.0, "tax_code": "ZERO", "weight": 0.1, "category": "ACCESSORIES"},
    ]

    stock = {"B100": 5, "G200": 10, "A300": 50}

    customer = {"id": "C001", "tier": "GOLD", "region": "MY", "loyalty_points": 1200}

    cart = [
        {"sku": "B100", "qty": 1},
        {"sku": "G200", "qty": 2},
        {"sku": "A300", "qty": 8},
    ]

    # === Process the Order ===
    try:
        order = process_order(catalog_data, stock, customer, cart)
    except ValueError as e:
        print(f"Order failed: {e}")
        return

    # === Display Summary ===
    print("=== ORDER SUMMARY ===")
    print(f"Subtotal (before discounts): RM {order['subtotal_before']:.2f}")
    print(f"Subtotal (after discounts):  RM {order['subtotal_after']:.2f}")
    print(f"Tax:                        RM {order['tax']:.2f}")
    print(f"Shipping:                   RM {order['shipping']:.2f}")
    print(f"Grand Total:                RM {order['grand_total']:.2f}")
    print(f"Points Earned:              {order['points_earned']}")

    # === Print Receipt Preview ===
    print("\n=== RECEIPT PREVIEW ===")
    receipt = generate_receipt(order)
    print(receipt)

    # === Export Results ===
    json_path, csv_path = export_order(order, "order.json", "order_lines.csv")
    print(f"\nFiles exported to:\n - {json_path}\n - {csv_path}")


if __name__ == "__main__":
    main()
