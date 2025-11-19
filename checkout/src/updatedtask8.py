from typing import Dict, Any

Customer = Dict[str, Any]

def compute_loyalty_points(net_total: float, customer: Customer) -> int:


    base_points = int(net_total // 5)

    tier = customer.get("tier", "").upper()
    if tier == "GOLD":
        bonus = int(base_points * 0.20)
    elif tier == "SILVER":
        bonus = int(base_points * 0.10)
    else:
        bonus = 0

    total_points = base_points + bonus

    return total_points
