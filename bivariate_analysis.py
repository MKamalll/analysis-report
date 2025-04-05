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
    cve, products, vendors = load_data()

    # Convert 'pub_date' to datetime and extract year
    cve['pub_date'] = pd.to_datetime(cve['pub_date'], errors='coerce')
    cve['pub_year'] = cve['pub_date'].dt.year

    cve = cve.dropna(subset=['cvss', 'pub_year'])

    # Scatter plot: pub_year vs cvss
    plt.scatter(cve['pub_year'], cve['cvss'])
    plt.title('Scatter Diagram: CVSS Score vs Publication Year')
    plt.xlabel('Publication Year')
    plt.ylabel('CVSS Score')
    plt.savefig('./figures/scatter_pub_year_vs_cvss.png')
    plt.show()

    # Pearson correlation
    correlation = cve[['pub_year', 'cvss']].corr(method='pearson')
    print("\nPearson Correlation between publication year and CVSS score:")
    print(correlation)

    # Cleanup
    del cve, products, vendors

# Entry Point
if __name__ == "__main__":
    main()