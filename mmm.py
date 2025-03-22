import pandas as pd
import numpy as np

# Import functions from other files
from cvss_categoriser import add_cvss_category
from dataset_loader import load_data



def main():
    """Main execution function."""
    print("Analysis and Reporting Module")

    # Load the data
    cve, products, vendor_product, vendors = load_data()

    # print the cve table info before processing the cvss values
    print(cve.info())

    # CVSS Analysis
    cve = add_cvss_category(cve)

    # print the cve table info after processing the cvss values
    print(cve.info())

    # Mohamed: Calculate Mode using pandas since stats does not support non numeric values
    mode_value = cve['cvss_category'].mode().values[0]  # Extract the mode value
    print(f"Mode of CVSS Category: {mode_value}")

    # Calculate Median for CVSS Scores
    median_value = np.median(cve['cvss'])
    print(f"Median CVSS Score: {median_value}")

    # Cleanup
    del cve, products, vendor_product, vendors

# Entry Point
if __name__ == "__main__":
    main()