import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    # Mohamed: Calculate Mode using pandas since stats does not support non numeric values
    mode_value = cve['cvss_category'].mode().values[0]  # Extract the mode value
    print(f"Mode of CVSS Category: {mode_value}")

    # Calculate Median for CVSS Scores
    median_value = np.median(cve['cvss'])
    print(f"Median CVSS Score: {median_value}")

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

    # Box Plot for CVSS Scores with IQR
    plt.figure(figsize=(8, 6))
    plt.boxplot(cve['cvss'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))

    # Add labels and title
    plt.title('Interquartile Range (IQR) of CVSS Scores')
    plt.xlabel('CVSS Score')

    # Annotate IQR on the plot
    plt.axvline(q1, color='orange', linestyle='--', label=f'Q1 = {q1:.2f}')
    plt.axvline(q3, color='green', linestyle='--', label=f'Q3 = {q3:.2f}')
    plt.axvline(median_value, color='red', linestyle='-', label=f'Median = {median_value:.2f}')
    plt.legend()
    plt.tight_layout()

    # Save the plot to file
    plt.savefig('./figures/IQR.png', dpi=300)  # You can change filename and dpi as needed

    plt.show()

    # Cleanup
    del cve, products, vendor_product, vendors

# Entry Point
if __name__ == "__main__":
    main()