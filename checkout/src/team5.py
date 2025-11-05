from typing import List, Dict, Tuple, Any

# 定义类型
CartItem = Dict[str, Any]  # 购物车项
Cart = List[CartItem]      # 购物车
DiscountBreakdown = List[Dict[str, Any]]  # 折扣明细

def apply_discounts(subtotal: float, cart: Cart, customer: Dict[str, Any]) -> Tuple[float, DiscountBreakdown]:
    discount_breakdown = []
    
    # 计算总数量
    total_qty = sum(item['qty'] for item in cart)
    
    # 应用 BULK10 折扣
    if total_qty >= 10:
        bulk_discount = subtotal * 0.10
        subtotal -= bulk_discount
        discount_breakdown.append({"rule": "BULK10", "amount": round(bulk_discount, 2)})
    
    # 应用 TIER 折扣
    tier_discount = 0
    if customer['tier'] == 'GOLD':
        tier_discount = subtotal * 0.05
    elif customer['tier'] == 'SILVER':
        tier_discount = subtotal * 0.02
    
    if tier_discount > 0:
        subtotal -= tier_discount
        discount_breakdown.append({"rule": "TIER", "amount": round(tier_discount, 2)})
    
    # 检查 BOOKS5 折扣
    if any(item['sku'] in catalog and catalog[item['sku']]['category'] == 'BOOKS' for item in cart):
        book_discount = 5.00
        subtotal -= book_discount
        discount_breakdown.append({"rule": "BOOKS5", "amount": round(book_discount, 2)})
    
    # 确保小计不为负数
    subtotal = max(0, subtotal)
    
    return round(subtotal, 2), discount_breakdown

# 示例数据
catalog = {
    "B100": {"sku": "B100", "name": "Intro to Python", "price": 50.0, "tax_code": "STD", "weight": 0.6, "category": "BOOKS"},
    "G200": {"sku": "G200", "name": "Gaming Mouse", "price": 80.0, "tax_code": "LUX", "weight": 0.2, "category": "GADGETS"},
    "A300": {"sku": "A300", "name": "Alkaline Batteries (4pk)", "price": 12.0, "tax_code": "ZERO", "weight": 0.1, "category": "ACCESSORIES"},
}

# 示例调用
subtotal = 100.0  # 假设的小计
cart = [{"sku": "B100", "qty": 5}, {"sku": "G200", "qty": 5}]  # 示例购物车
customer = {"id": "C001", "tier": "GOLD", "region": "MY", "loyalty_points": 1200}  # 示例客户

new_subtotal, discounts = apply_discounts(subtotal, cart, customer)
print("新小计:", new_subtotal)
print("折扣明细:", discounts)
