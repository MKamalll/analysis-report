import pandas as pd

def load_data():

    """Load and return CSV data files."""
    cve = pd.read_csv('./archive/cve.csv')
    cve_cleaned = cleanup(cve)
    products = pd.read_csv('./archive/products.csv')
    vendor_product = pd.read_csv('./archive/vendor_product.csv')
    vendors = pd.read_csv('./archive/vendors.csv')    
    return cve_cleaned, products, vendor_product, vendors


def cleanup(cve):

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
    print(f"Rows before cleaning: {before_cleaning}")

    # Remove rows with missing (NaN) or empty ("") values in the specified columns
    cve_cleaned = cve.dropna(subset=columns_to_check)

    # Report the number of rows after cleaning
    after_cleaning = len(cve_cleaned)
    delta = before_cleaning - after_cleaning

    print(f"Rows after cleaning: {after_cleaning}")
    print(f"Rows removed (cleaned): {delta}")

    # Remove duplicate CVE IDs
    before_dedup = len(cve_cleaned)
    cve_cleaned = cve_cleaned.drop_duplicates(subset=cve_cleaned.columns[0])  # Assuming CVE ID is the first column
    after_dedup = len(cve_cleaned)
    duplicates_removed = before_dedup - after_dedup
    print(f"Duplicate CVE entries removed: {duplicates_removed}")



    return cve_cleaned