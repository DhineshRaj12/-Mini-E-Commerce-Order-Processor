def load_catalog(products):
    required_keys = {'sku', 'name', 'price', 'tax_code', 'weight', 'category'}
    catalog = {}
    
    for product in products:
        # Validate required keys
        if not required_keys.issubset(product.keys()):
            missing_keys = required_keys - product.keys()
            raise ValueError(f"Product missing required keys: {missing_keys}")
        
        # Create a cleaned copy of the product
        cleaned_product = product.copy()
        
        # Convert SKU to lowercase
        cleaned_product['sku'] = str(product['sku']).lower()
        
        # Convert price and weight to float
        try:
            cleaned_product['price'] = float(product['price'])
        except (ValueError, TypeError):
            raise ValueError(f"Invalid price value for SKU {cleaned_product['sku']}: {product['price']}")
        
        try:
            cleaned_product['weight'] = float(product['weight'])
        except (ValueError, TypeError):
            raise ValueError(f"Invalid weight value for SKU {cleaned_product['sku']}: {product['weight']}")
        
        # Convert tax_code to lowercase
        cleaned_product['tax_code'] = str(product['tax_code']).lower()
        
        # Use lowercase SKU as key in catalog
        sku = cleaned_product['sku']
        catalog[sku] = cleaned_product
    
    return catalog
