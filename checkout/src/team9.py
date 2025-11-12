from typing import Dict, Any, List

DiscountBreakdown = List[Dict[str, Any]]

def generate_receipt(order: Dict[str, Any]) -> str:
    """
    Input: 'order' dictionary containing:
        - customer, cart, catalog
        - subtotal_before, subtotal_after, discount_breakdown
        - tax, shipping, grand_total, points_earned
    Output: multi-line string summarizing the order.
    """
    customer = order["customer"]
    cart = order["cart"]
    catalog = order["catalog"]
    discount_breakdown: DiscountBreakdown = order.get("discount_breakdown", [])

    lines = []
    lines.append("=" * 50)
    lines.append(f"RECEIPT for Customer ID: {customer['id']} ({customer.get('tier', '')})")
    lines.append("=" * 50)
    lines.append(f"{'SKU':<8} {'Name':<25} {'Qty':>3} {'Price':>8} {'Total':>10}")
    lines.append("-" * 50)

    for item in cart:
        sku = item["sku"]
        product = catalog[sku]
        qty = item["qty"]
        price = product["price"]
        total = price * qty
        lines.append(f"{sku:<8} {product['name'][:25]:<25} {qty:>3} {price:>8.2f} {total:>10.2f}")

    lines.append("-" * 50)
    lines.append(f"{'Subtotal (before discounts)':<40}{order['subtotal_before']:>10.2f}")
    lines.append(f"{'Subtotal (after discounts)':<40}{order['subtotal_after']:>10.2f}")

    if discount_breakdown:
        lines.append("  Discounts Applied:")
        for d in discount_breakdown:
            lines.append(f"    - {d['rule']:<20} -RM {d['amount']:.2f}")

    lines.append(f"{'Tax':<40}{order['tax']:>10.2f}")
    lines.append(f"{'Shipping':<40}{order['shipping']:>10.2f}")
    lines.append("=" * 50)
    lines.append(f"{'GRAND TOTAL':<40}RM {order['grand_total']:>8.2f}")
    lines.append(f"{'Points Earned':<40}{order['points_earned']:>10}")
    lines.append("=" * 50)

    return "\n".join(lines)
