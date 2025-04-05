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

    # --- Encode categorical variables and compute correlation ---
    
    # Reload CVE data
    cve, _, _ = load_data()
    
    # Select categorical columns
    categorical_cols = ['access_authentication', 'access_complexity', 'access_vector',
                        'impact_availability', 'impact_confidentiality', 'impact_integrity']
        
    # Encode categories as numeric using pandas factorize
    for col in categorical_cols:
        cve[col + '_num'], _ = pd.factorize(cve[col])
    
    # Add the encoded columns to a new DataFrame
    encoded_df = cve[['cvss'] + [col + '_num' for col in categorical_cols]]
    
    # Compute Pearson correlation
    encoded_corr = encoded_df.corr(method='pearson')
    print("\nPearson Correlation Matrix (CVSS vs Encoded Categorical Features):")
    print(encoded_corr)
    
    # Plot scatter diagrams for each categorical feature vs cvss
    for col in categorical_cols:
        plt.scatter(cve[col + '_num'], cve['cvss'])
        plt.title(f'Scatter Diagram: CVSS Score vs {col}')
        plt.xlabel(f'{col} (encoded)')
        plt.ylabel('CVSS Score')
        plt.savefig(f'./figures/scatter_cvss_vs_{col}.png')
        plt.show()
    
    # --- Additional analysis: access_complexity vs impact metrics ---
    impact_metrics = ['impact_availability_num', 'impact_confidentiality_num', 'impact_integrity_num']
    for impact in impact_metrics:
        plt.scatter(cve['access_complexity_num'], cve[impact])
        plt.title(f'Scatter Diagram: Access Complexity vs {impact}')
        plt.xlabel('Access Complexity (encoded)')
        plt.ylabel(f'{impact}')
        plt.savefig(f'./figures/scatter_access_complexity_vs_{impact}.png')
        plt.show()

    # Pearson correlations
    print("\nPearson Correlation: Access Complexity vs Impact Metrics")
    for impact in impact_metrics:
        r = cve[['access_complexity_num', impact]].corr(method='pearson').iloc[0,1]
        print(f"Access Complexity vs {impact}: r = {r:.3f}")

    # Cleanup
    del cve, products, vendors

# Entry Point
if __name__ == "__main__":
    main()