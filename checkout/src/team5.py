from typing import List, Dict, Tuple, Any

CartItem = Dict[str, Any]
Cart = List[CartItem]
DiscountBreakdown = List[Dict[str, Any]]

def apply_discounts(subtotal: float, cart: Cart, customer: Dict[str, Any]) -> Tuple[float, DiscountBreakdown]:
    
    discount_breakdown: DiscountBreakdown = []
    new_subtotal = subtotal

    # --- BULK10 ---
    total_qty = sum(item.get("qty", 0) for item in cart)
    if total_qty >= 10:
        bulk_discount = round(new_subtotal * 0.10, 2)
        new_subtotal -= bulk_discount
        discount_breakdown.append({"rule": "BULK10", "amount": bulk_discount})

    # --- TIER ---
    tier = customer.get("tier", "").upper()
    tier_discount_rate = 0.05 if tier == "GOLD" else (0.02 if tier == "SILVER" else 0)
    if tier_discount_rate > 0:
        tier_discount = round(new_subtotal * tier_discount_rate, 2)
        new_subtotal -= tier_discount
        discount_breakdown.append({"rule": "TIER", "amount": tier_discount})

    # --- BOOKS5 ---
    if any(item.get("category", "").upper() == "BOOKS" for item in cart):
        book_discount = 5.00
        new_subtotal -= book_discount
        new_subtotal = max(0, new_subtotal)
        discount_breakdown.append({"rule": "BOOKS5", "amount": round(book_discount, 2)})

    new_subtotal = round(max(new_subtotal, 0), 2)
    return new_subtotal, discount_breakdown

