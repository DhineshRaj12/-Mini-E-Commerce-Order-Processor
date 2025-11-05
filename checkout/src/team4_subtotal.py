def calculate_subtotal(cart: dict, catalog: dict) -> float:
    """
    - Sum price * qty for all cart items (use catalog price).
    - Round to 2 decimals at the end (banker's rounding not required).
    Example:
        cart = {"P100": 3, "P300": 2}
        catalog = {"P100": 10.0, "P300": 2.5}
        → subtotal = 35.00
    """
    subtotal = 0.0
    for product_id, qty in cart.items():
        price = catalog.get(product_id, 0.0)
        subtotal += price * qty

    return f"{subtotal:.2f}"

cart = {"P100": 3, "P300": 2}
catalog = {"P100": 10.0, "P300": 2.5}

print(calculate_subtotal(cart, catalog))  # Output: 35.00
