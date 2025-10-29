"""
pipeline.py — Integration pipeline for Mini E-Commerce Order Processor

This file orchestrates the full order flow:
1. Loads and validates catalog  (Team 1)
2. Sanitizes and merges cart    (Team 2)
3. Checks stock availability    (Team 3)
4. Computes subtotal            (Team 4)
5. Applies discounts            (Team 5)
6. Calculates tax               (Team 6)
7. Estimates shipping           (Team 7)
8. Calculates loyalty points    (Team 8)
9. Returns final order data     (for Team 9 and Team 10)
"""

from typing import Dict, Any
from checkout.src.team1_catalog import load_catalog
from checkout.src.team2_cart import sanitize_cart
from checkout.src.team3_inventory import validate_inventory
from checkout.src.team4_subtotal import calculate_subtotal
from checkout.src.team5_discounts import apply_discounts
from checkout.src.team6_tax import compute_tax
from checkout.src.team7_shipping import compute_shipping
from checkout.src.team8_loyalty import compute_loyalty_points


def process_order(
    catalog_data: list,
    stock: Dict[str, int],
    customer: Dict[str, Any],
    cart: list,
) -> Dict[str, Any]:
    """
    Main integration pipeline — executes all steps in order.
    Returns the final `order` dictionary ready for receipt/export.
    Raises ValueError if inventory validation fails.
    """

    # === Step 1: Load and validate catalog ===
    catalog = load_catalog(catalog_data)

    # === Step 2: Clean and merge cart ===
    cart = sanitize_cart(cart, catalog)

    # === Step 3: Check inventory ===
    ok, issues = validate_inventory(cart, stock)
    if not ok:
        raise ValueError(f"Inventory issues: {issues}")

    # === Step 4: Compute subtotal ===
    subtotal_before = calculate_subtotal(cart, catalog)

    # === Step 5: Apply discounts ===
    subtotal_after, discount_breakdown = apply_discounts(subtotal_before, cart, customer)

    # === Step 6: Compute tax ===
    tax = compute_tax(cart, catalog, customer["region"])

    # === Step 7: Compute shipping ===
    shipping = compute_shipping(cart, catalog, customer["region"])

    # === Step 8: Calculate final totals and loyalty ===
    grand_total = round(subtotal_after + tax + shipping, 2)
    points_earned = compute_loyalty_points(grand_total, customer)

    # === Step 9: Build the final order dict ===
    order = {
        "customer": customer,
        "cart": cart,
        "catalog": catalog,
        "subtotal_before": round(subtotal_before, 2),
        "subtotal_after": round(subtotal_after, 2),
        "discount_breakdown": discount_breakdown,
        "tax": tax,
        "shipping": shipping,
        "grand_total": grand_total,
        "points_earned": points_earned,
    }

    return order
