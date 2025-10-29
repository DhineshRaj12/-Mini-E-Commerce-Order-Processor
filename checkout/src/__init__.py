"""
checkout.src package

Contains all the core team modules for the checkout pipeline.
Each module implements a specific part of the e-commerce process.
"""

from checkout.src.team1_catalog import load_catalog
from checkout.src.team2_cart import sanitize_cart
from checkout.src.team3_inventory import validate_inventory
from checkout.src.team4_subtotal import calculate_subtotal
from checkout.src.team5_discounts import apply_discounts
from checkout.src.team6_tax import compute_tax
from checkout.src.team7_shipping import compute_shipping
from checkout.src.team8_loyalty import compute_loyalty_points
from checkout.src.team9_receipt import generate_receipt
from checkout.src.team10_export import export_order
from checkout.src.pipeline import process_order

__all__ = [
    "load_catalog",
    "sanitize_cart",
    "validate_inventory",
    "calculate_subtotal",
    "apply_discounts",
    "compute_tax",
    "compute_shipping",
    "compute_loyalty_points",
    "generate_receipt",
    "export_order",
    "process_order",
]
