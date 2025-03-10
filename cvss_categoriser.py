import pandas as pd
import matplotlib.pyplot as plt

def categorise_cvss(score):
    """Categorise CVSS scores into risk levels."""
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

def add_cvss_category(cve_df):
    """Add the CVSS category column to the DataFrame."""
    cve_df['cvss_category'] = cve_df['cvss'].apply(categorise_cvss)
    return cve_df

def cvss_statistics(cve_df):
    """ """
    cvss_counts_df = cve_df['cvss_category'].value_counts().reset_index(name='Count')
    cvss_counts_df.columns = ['CVSS Category', 'Count']

    # Display results
    print(cvss_counts_df)
    return cvss_counts_df

def cvss_show(cvss_counts):
    """ draw the figure and save it in figures folder """
    """ Bar chart visualization """
    plt.figure(figsize=(8, 5))
    plt.bar(cvss_counts['CVSS Category'], cvss_counts['Count'], 
            color=['red', 'orange', 'yellow', 'green', 'gray'])

    plt.title('CVSS Score Distribution')
    plt.xlabel('CVSS Category')
    plt.ylabel('Number of CVEs')
    plt.savefig('./figures/cvsscount.png',dpi=300,transparent=True)
    plt.show()
