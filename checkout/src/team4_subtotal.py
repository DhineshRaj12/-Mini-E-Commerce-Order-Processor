from typing import Dict, List, Tuple, Any

# --- Type Aliases ---
CartItem = Dict[str, Any]  # individual item with 'sku' and 'qty'
Cart = List[CartItem]      # list of CartItem
Stock = Dict[str, int]     # e.g. {'P100': 10, 'P300': 4}
Catalog = Dict[str, float] # e.g. {'P100': 10.0, 'P300': 2.5}

# --- Subtotal Calculation ---
def calculate_subtotal(cart: Cart, catalog: Catalog) -> float:
    """
    Calculate subtotal by summing price * qty for all cart items.
    Round to 2 decimals at the end.
    """
    subtotal = 0.0
    for item in cart:
        sku = item.get('sku')
        qty = item.get('qty', 0)
        price = catalog.get(sku, 0.0)
        subtotal += price * qty

    return f"{subtotal:.2f}"
