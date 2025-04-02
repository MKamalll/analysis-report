import pandas as pd
from cvss_categoriser import add_cvss_category

def load_data():

    # Load and return CSV data files.
    print(f"Load Dataset Function Call! ")
    cve = pd.read_csv('./dataset/cve.csv')  
    products = pd.read_csv('./dataset/products.csv')
    vendor_product = pd.read_csv('./dataset/vendor_product.csv')
    vendors = pd.read_csv('./dataset/vendors.csv')  

    # Cleanup Function Call!
    cve_cleaned, products_cleaned, vendor_product_cleaned, vendors_cleaned = cleanup(cve, products, vendor_product, vendors)

    # CVSS categorisation # this will add a new column to the dataset to annotate the cvss score to a rating either Low, Medium, High, Critical
    cve_cleaned = add_cvss_category(cve_cleaned)
    
    return cve_cleaned, products_cleaned, vendor_product_cleaned, vendors_cleaned


def cleanup(cve, products, vendor_product, vendors):

    print(f"Cleanup Function Call! ")
    
    # Define the columns to check for missing/empty values
    columns_to_check = [
        'mod_date',
        'pub_date',
        'cvss',
        'cwe_code',
        'cwe_name',
        'summary',
        'access_authentication',
        'access_complexity',
        'access_vector',
        'impact_availability',
        'impact_confidentiality',
        'impact_integrity'
    ]

    # Report the number of rows before cleaning
    before_cleaning = len(cve)

    # Remove rows with missing (NaN) values in the specified columns
    cve_cleaned = cve.dropna(subset=columns_to_check)

    # Report the number of rows after cleaning
    after_cleaning = len(cve_cleaned)
    delta = before_cleaning - after_cleaning

    #print(f"Rows after cleaning: {after_cleaning}")
    print(f"CVEs - rows removed (cleaned): {delta}")

    # Remove duplicate CVE IDs
    before_dedup = len(cve_cleaned)
    cve_cleaned = cve_cleaned.drop_duplicates(subset=cve_cleaned.columns[0])  # Assuming CVE ID is the first column
    after_dedup = len(cve_cleaned)
    duplicates_removed = before_dedup - after_dedup
    print(f"Duplicate CVE entries removed: {duplicates_removed}")

    # Clean products DataFrame
    products_cleaned = products.dropna(subset=['cve_id', 'vulnerable_product'])
    print(f"Products - rows removed: {len(products) - len(products_cleaned)}")

    # Clean vendor_product DataFrame
    vendor_product_cleaned = vendor_product.dropna(subset=['vendor', 'product'])
    print(f"Vendor_Product - rows removed: {len(vendor_product) - len(vendor_product_cleaned)}")

    # Clean vendors DataFrame
    vendors_cleaned = vendors.dropna(subset=['vendor'])
    print(f"Vendors - rows removed: {len(vendors) - len(vendors_cleaned)}")

    # I want to print some blank space before entering the new feature
    print("\n\n\n\n")
          
    return cve_cleaned, products_cleaned, vendor_product_cleaned, vendors_cleaned