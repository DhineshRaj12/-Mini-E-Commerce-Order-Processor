from typing import Dict, List, Any

Cart = List[Dict[str, Any]]
Catalog = Dict[str, Dict[str, Any]]

def compute_tax(cart: Cart, catalog: Catalog, region: str) -> float:

    tax_rates = {'std': 0.06, 'zero': 0.0, 'lux': 0.10}

    pre_total = sum(catalog[item['sku']]['price'] * item['qty'] for item in cart if item['sku'] in catalog)
    if pre_total <= 0:
        return 0.0

    
        discount_ratio = 1.0  

    total_tax = 0.0
    for item in cart:
        sku = item.get('sku')
        qty = item.get('qty', 0)
        if sku not in catalog:
            continue
        product = catalog[sku]
        rate = tax_rates.get(product.get('tax_code', 'std').lower(), 0.0)
        line_total = product['price'] * qty * discount_ratio
        total_tax += line_total * rate

    return round(total_tax, 2)
