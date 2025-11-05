{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d138dca-7c49-4aee-ab6d-99e2ed68f310",
   "metadata": {},
   "outputs": [],
   "source": [
    "from typing import Dict, List, Tuple, Any\n",
    "\n",
    "CartItem = Dict[str, Any]\n",
    "Cart = List[CartItem]\n",
    "Stock = Dict[str, int]\n",
    "\n",
    "\n",
    "def validate_inventory(cart: Cart, stock: Stock) -> Tuple[bool, List[str]]:\n",
    "\n",
    "    issues: List[str] = []\n",
    "\n",
    "    for item in cart:\n",
    "        sku = item.get('sku')\n",
    "        qty = item.get('qty', 0)\n",
    "\n",
    "        # 1. Get stock level; if SKU missing, treat as 0\n",
    "        available = stock.get(sku, 0)\n",
    "\n",
    "        # 2. Check stock sufficiency\n",
    "        if qty > available:\n",
    "            issues.append(\n",
    "                f\"Insufficient stock for {sku}: requested {qty}, available {available}\"\n",
    "            )\n",
    "\n",
    "    ok = len(issues) == 0\n",
    "    return ok, issues"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
