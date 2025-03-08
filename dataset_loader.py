import pandas as pd

def load_data():
    """Load and return CSV data files."""
    cve = pd.read_csv('./archive/cve.csv')
    products = pd.read_csv('./archive/products.csv')
    vendor_product = pd.read_csv('./archive/vendor_product.csv')
    vendors = pd.read_csv('./archive/vendors.csv')    
    return cve, products, vendor_product, vendors