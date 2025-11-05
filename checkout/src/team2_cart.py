from typing import Dict, List, Any

# Shared data types (as per context)
Cart = List[Dict[str, Any]]
Catalog = Dict[str, Dict[str, Any]]

def sanitize_cart(cart: Cart, catalog: Catalog) -> Cart:
    """
    - Remove items with invalid SKUs (not present in catalog).
    - Merge duplicates (same sku) by summing qty.
    - Drop items with qty <= 0.
    - Return a clean, normalized cart.
    """
    # Input validation (added for robustness, as per test expectations)
    if not isinstance(cart, list):
        raise TypeError("cart must be a list")
    if not isinstance(catalog, dict):
        raise TypeError("catalog must be a dict")
    
    qty_dict = {}
    for item in cart:
        if not isinstance(item, dict):
            continue  # Skip invalid items silently (or raise if preferred)
        sku = item.get("sku")
        qty = item.get("qty", 0)
        # Ensure qty is numeric; treat non-numeric as 0
        try:
            qty = int(qty) if isinstance(qty, (int, float)) else 0
        except (ValueError, TypeError):
            qty = 0
        if sku in catalog and qty > 0:
            qty_dict[sku] = qty_dict.get(sku, 0) + qty
    # Return as list of dicts, preserving insertion order (Python 3.7+ dict order)
    return [{"sku": sku, "qty": qty} for sku, qty in qty_dict.items()]