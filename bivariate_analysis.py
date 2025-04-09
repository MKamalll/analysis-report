import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm

# Import functions from other files
from dataset_loader import load_data



def bivariate_analysis(cve):

    print("Bivariate Analysis \n")
    print("    -------------------     ")

    # Convert 'pub_date' to datetime and extract year
    cve['pub_date'] = pd.to_datetime(cve['pub_date'], errors='coerce')
    cve['pub_year'] = cve['pub_date'].dt.year

    
    # Select categorical columns
    categorical_cols = ['pub_year','impact_availability', 'impact_confidentiality', 'impact_integrity']
        
    # Encode categories as numeric using pandas factorize
    for col in categorical_cols:
        if cve[col].dtype == 'object':
            cve[col + '_num'], _ = pd.factorize(cve[col])
        else:
            cve[col + '_num'] = cve[col]
    
    # Encode 'cwe_name' text to numeric labels
    cve['cwe_name_encoded'] = LabelEncoder().fit_transform(cve['cwe_name'].astype(str))
    
    # Add the encoded columns to a new DataFrame
    encoded_df = cve[['cvss', 'cwe_name_encoded'] + [col + '_num' for col in categorical_cols]]
    
    # Compute Pearson correlation
    encoded_corr = encoded_df.corr(method='pearson')
    print("\nPearson Correlation Matrix (CVSS vs Encoded Features including CWE Name):")
    print(encoded_corr)
    
    # Plot scatter diagrams for each encoded feature vs cvss
    for col in encoded_df.columns:
        if col != 'cvss':
            plt.scatter(encoded_df[col], encoded_df['cvss'],color='#0570b0')
            plt.title(f'Scatter Diagram: CVSS Score vs {col}')
            plt.xlabel(f'{col}')
            plt.ylabel('CVSS Score')
            plt.savefig(f'./figures/scatter_cvss_vs_{col}.png')
            plt.show()
    
    
    # Perform linear regression between cwe_name_encoded and cvss
    X = sm.add_constant(cve['cwe_name_encoded'])
    model = sm.OLS(cve['cvss'], X).fit()
    print("\nLinear Regression Summary (CVSS ~ CWE Name Encoded):")
    print(model.summary())