import pandas as pd

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