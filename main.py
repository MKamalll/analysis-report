import pandas as pd
import numpy as np
import statsmodels as sm
import scipy
import matplotlib.pyplot as plt
import pymc as pm
from dataset_loader import load_data
from cvss_categoriser import add_cvss_category

# functions
def printCVE():
    """Display basic CVE information."""
    print("Files are loaded")
    #print(cve.head())
    print(cve.info())
    #print(cve.describe())
    #print(cve.shape)

# Function to categorize CVSS scores
def categorize_cvss(score):
    if score >= 9.0:
        return 'Critical'
    elif 7.0 <= score < 9.0:
        return 'High'
    elif 4.0 <= score < 7.0:
        return 'Medium'
    elif 1.0 <= score < 4.0:
        return 'Low'
    else:
        return 'None'


# Main Function
def main():
    """Main execution function."""
    print("Analysis and Reporting Module")

    # Load the data
    cve, products, vendor_product, vendors = load_data()

    # Categorize CVSS scores
    cve = add_cvss_category(cve)

    # CVSS Statistics
    cvss_counts = cve['cvss_category'].value_counts().reset_index(name='Count')
    cvss_counts.columns = ['CVSS Category', 'Count']

    # Display results
    print(cvss_counts)

    # Bar chart visualization
    plt.figure(figsize=(8, 5))
    plt.bar(cvss_counts['CVSS Category'], cvss_counts['Count'], 
            color=['red', 'orange', 'yellow', 'green', 'gray'])

    plt.title('CVSS Score Distribution')
    plt.xlabel('CVSS Category')
    plt.ylabel('Number of CVEs')
    plt.show()

    # Print CVE details
    printCVE(cve)

    # Cleanup
    del cve, products, vendor_product, vendors

# Entry Point
if __name__ == "__main__":
    main()