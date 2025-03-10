import pandas as pd
import numpy as np
import statsmodels as sm
import scipy
import matplotlib.pyplot as plt
import pymc as pm

# import functions from other files
from dataset_loader import load_data
from cvss_categoriser import add_cvss_category
from cvss_categoriser import cvss_statistics
from cvss_categoriser import cvss_show

from vendors_parser import vendors_statistics
from vendors_parser import vendors_show

from cwe_parser import cwes_statistics
from cwe_parser import cwes_show

# functions
def printCVE(cve):
    """Display basic CVE information."""
    print("Files are loaded")
    #print(cve.head())
    print(cve.info())
    #print(cve.describe())
    #print(cve.shape)

# Main Function
def main():
    """Main execution function."""
    print("Analysis and Reporting Module")

    # Load the data
    cve, products, vendor_product, vendors = load_data()

    """ CVSS """
    # Categorize CVSS scores
    cve = add_cvss_category(cve)

    # CVSS Statistics
    cvss_counts= cvss_statistics(cve)

    #cvss_show(cvss_counts)
    """ CVSS End """

    # Print CVE details
    printCVE(vendors)


    """ Vendors Statistics """
    #vendors_count = vendors_statistics(vendors)

    #vendors_show(vendors_count)

    """ cwes Statistics """
    cwes_count = cwes_statistics(cve)

    cwes_show(cwes_count)

    """cleanup""" 
    del cve, products, vendor_product, vendors, cvss_counts

# Entry Point
if __name__ == "__main__":
    main()