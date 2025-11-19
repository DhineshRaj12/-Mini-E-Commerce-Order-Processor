from typing import Dict, Any, List

Cart = List[Dict[str, Any]]
Catalog = Dict[str, Dict[str, Any]]

def compute_shipping(cart: Cart, catalog: Catalog, region: str, subtotal_after_discount: float) -> float:

    # Free shipping rule
    if subtotal_after_discount >= 150:
        return 0.0

    #Calculate total weight
    total_weight = 0.0
    for item in cart:
        sku = item["sku"]
        qty = item["qty"]
        weight = catalog[sku]["weight"]
        total_weight += weight * qty

    #Apply weight-based shipping
    if total_weight <= 1.0:
        cost = 6.0
    elif total_weight <= 5.0:
        cost = 12.0
    else:
        cost = 25.0

    return round(cost, 2)
