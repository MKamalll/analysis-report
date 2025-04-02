import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import functions from other files
from dataset_loader import load_data



def main():
    # Main execution function
    print("\n\n")
    print("Analysis and Reporting Module\n")
    print("    ----------------------     ")

    # Load the data
    cve, products, vendor_product, vendors = load_data()

    # Debugging: print the cve table info before processing the cvss values
    #print(cve.info())

    print("Univariate Analysis \n")
    print("    -------------------     ")

    # Calculate Median for CVSS Scores
    median_value = np.median(cve['cvss'])
    print(f"Median CVSS Score: {median_value}")

    # Mohamed: Calculate Mode using pandas since stats does not support non numeric values
    mode_value = cve['cvss_category'].mode().values[0]  # Extract the mode value
    print(f"Mode of CVSS Category: {mode_value}")

    # Additional Statistical Analysis

    # 1. Range and Standard Deviation
    cvss_range = cve['cvss'].max() - cve['cvss'].min()
    cvss_std = np.std(cve['cvss'])  
    print(f"Range of CVSS Scores: {cvss_range}")
    print(f"Standard Deviation of CVSS Scores: {cvss_std}")

    # 2. Dispersion Analysis
    print("\nDispersion Summary:")
    print(cve['cvss'].describe())

    # 3. Interquartile Range (IQR)
    q1 = np.percentile(cve['cvss'], 25)
    q3 = np.percentile(cve['cvss'], 75)
    iqr = q3 - q1
    print(f"Interquartile Range (IQR) of CVSS Scores: {iqr}")
    print("\n\n")
    
    # Box Plot for CVSS Scores with IQR
    # boxplot (just plotting cvss distribution)
    plt.figure(figsize=(6, 6))
    cve.boxplot(column='cvss')
    plt.title('Boxplot of CVSS Scores')
    plt.ylabel('CVSS Score')
    plt.tight_layout()

    # Save the plot to file
    plt.savefig('./figures/IQR.png', dpi=300)
    plt.show()

    # Cleanup
    del cve, products, vendor_product, vendors

# Entry Point
if __name__ == "__main__":
    main()