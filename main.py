import pandas as pd
import numpy as np
import statsmodels.api as sm  # Correct import for statsmodels
import scipy
import matplotlib.pyplot as plt
import pymc as pm

# Import functions from other files
from dataset_loader import load_data
from cvss_categoriser import add_cvss_category, cvss_statistics, cvss_show
from vendors_parser import vendors_statistics, vendors_show
from cwe_parser import cwes_statistics, cwes_show
from cve_parser import count_cves_per_year, cves_show,attack_vector_parse,impact_parse

def print_cve_info(cve):
    """Display basic CVE information."""
    print("Files are loaded")
    print(cve.info())

def main():
    """Main execution function."""
    print("Analysis and Reporting Module")

    # Load the data
    cve, products, vendor_product, vendors = load_data()

    # CVSS Analysis
    cve = add_cvss_category(cve)
    cvss_counts = cvss_statistics(cve)
    # cvss_show(cvss_counts)

    # Print CVE details
    print_cve_info(vendors)

    # Vendors Analysis
    # vendors_count = vendors_statistics(vendors)
    # vendors_show(vendors_count)

    # CWE Analysis
    cwes_count = cwes_statistics(cve)
    # cwes_show(cwes_count)

    # CVEs per Year
    cves_per_year = count_cves_per_year(cve)
    cves_show(cves_per_year)

    # Attack Vector Statistics
    attack_vector_parse(cve)

    # Impact Statistics
    impact_parse(cve)
    
    # Cleanup
    del cve, products, vendor_product, vendors, cvss_counts

# Entry Point
if __name__ == "__main__":
    main()