from typing import Dict, List, Tuple, Any

CartItem = Dict[str, Any]
Cart = List[CartItem]
Stock = Dict[str, int]


def validate_inventory(cart: Cart, stock: Stock) -> Tuple[bool, List[str]]:

    issues: List[str] = []

    for item in cart:
        sku = item.get('sku')
        qty = item.get('qty', 0)

        available = stock.get(sku, 0)

        if qty > available:
            issues.append(
                f"Insufficient stock for {sku}: requested {qty}, available {available}"
            )

    ok = len(issues) == 0
    return ok, issues
