import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import functions from other files
from dataset_loader import load_data
from cvss_categoriser import add_cvss_category, cvss_statistics, cvss_show
from vendors_parser import vendors_statistics, vendors_show
from cwe_parser import cwes_statistics, cwes_show
from cve_parser import count_cves_per_year, cves_show,impact_parse,impact_parse_grouped,vulnerable_product_parser
from access_authentication import access_authentication_statistics
from access_complexity import access_complexity_statistics
from attack_vector import attack_vector_statistics
from univariate_analysis import univariate_analysis
from bivariate_analysis import bivariate_analysis

def print_cve_info(cve):
    """Display basic CVE information."""
    print("Files are loaded")
    print(cve.info())

def main():
    # Main execution function
    print("Analysis and Reporting Module")
    print("===================================\n")

    # Load the data and clean it
    cve, products, vendors = load_data()

    # CVSS Analysis
    cvss_counts = cvss_statistics(cve)
    cvss_show(cvss_counts)

    # Print CVE details
    # print_cve_info(vendors)

    # Vendors Analysis
    vendors_count = vendors_statistics(vendors)
    vendors_show(vendors_count)

    # CWE Analysis
    cwes_count = cwes_statistics(cve)
    cwes_show(cwes_count)
    
    # CVEs per Year
    cves_per_year = count_cves_per_year(cve)
    cves_show(cves_per_year)

    # Attack Vector Statistics
    attack_vector_statistics(cve)

    # Access Authentication Statistics
    access_authentication_statistics(cve)	
    
    # Access Complexity Statistics
    access_complexity_statistics(cve)

    # Attack Vector Statistics
    attack_vector_statistics(cve)

    # Impact Statistics
    impact_parse(cve)
    impact_parse_grouped(cve)
    
    # vulnerable products
    print(products.columns)
    vulnerable_product_parser(products)

    #univariate analysis
    univariate_analysis(cve)

    # Bivariate Analysis
    bivariate_analysis(cve)

    # Cleanup
    del cve, products, vendors, cvss_counts

# Entry Point
if __name__ == "__main__":
    main()