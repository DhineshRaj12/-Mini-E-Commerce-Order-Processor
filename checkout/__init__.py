"""
checkout package

This is the root package for the Mini E-Commerce Order Processor.
It exposes the main pipeline and key modules for easier importing.
"""

from checkout.src.pipeline import process_order
from checkout.src.team9_receipt import generate_receipt
from checkout.src.team10_export import export_order

__all__ = ["process_order", "generate_receipt", "export_order"]
