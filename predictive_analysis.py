import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# Import functions from other files
from dataset_loader import load_data



def predictive_analysis(cve):

    print("Predictive Analysis \n")
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
    

    # Perform linear regression between cwe_name_encoded and cvss
    model = LinearRegression()
    X = encoded_df[['cwe_name_encoded']]
    y = encoded_df['cvss']
    model.fit(X, y)

    # Extract the weight (slope) and constant (intercept) 
    # following webinar 6 slides
    weighting = model.coef_[0] 
    constant = model.intercept_

    # Print the predictions and R-squared value        
    print("\nLinear Regression Summary (CVSS vs CWE-name):")
    print(f"Weight (Slope): {weighting:.2f}")
    print(f"Constant (Intercept): {constant:.2f}")
    print(f"R-squared: {model.score(X, y)}")

    # Add predictions to the DataFrame
    encoded_df['cvss_pred'] = model.predict(X)

    # Plot the regression line
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color='#4D648D', label='Actual Data')
    plt.plot(X, weighting * X + constant, color='red', linewidth=2, label=f'Regression Line: y = {weighting:.2f}x + {constant:.2f}')
    plt.title('Linear Regression: CVSS Score vs CWE Name Encoded')
    plt.xlabel('CWE Name Encoded')
    plt.ylabel('CVSS Score')
    plt.legend()
    plt.savefig('./figures/linear_regression_cvss_vs_cwe_name_encoded.png')
    plt.show()

    # Linear Regression: CVSS vs Publication Year
    X_year = encoded_df[['pub_year_num']]
    y_year = encoded_df['cvss']
    model_year = LinearRegression()
    model_year.fit(X_year, y_year)

    weighting_year = model_year.coef_[0]
    constant_year = model_year.intercept_

    encoded_df['cvss_pred_year'] = model_year.predict(X_year)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_year, y_year, color='#4D648D', label='Actual Data')
    plt.plot(X_year, model_year.predict(X_year), color='red', linewidth=2,
             label=f'Regression Line: y = {weighting_year:.2f}x + {constant_year:.2f}')
    plt.title('Linear Regression: CVSS Score vs Publication Year')
    plt.xlabel('Publication Year')
    plt.ylabel('CVSS Score')
    plt.legend()
    plt.savefig('./figures/linear_regression_cvss_vs_pub_year.png')
    plt.show()

    print("\nLinear Regression Summary (CVSS vs Publication Year):")
    print(f"Weight (Slope): {weighting_year:.2f}")
    print(f"Constant (Intercept): {constant_year:.2f}")
    print(f"R-squared: {model_year.score(X_year, y_year):.2f}")
