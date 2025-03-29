import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import functions from other files
from dataset_loader import load_data

# Load the data
cve, products, vendor_product, vendors = load_data()

# Ensure required columns exist before mapping
required_columns = ['cvss', 'impact_availability', 'impact_confidentiality', 'impact_integrity']

# Filter dataset to include only relevant columns
df = cve[required_columns].copy()

# Mapping Categorical Values to Numeric Values
impact_mapping = {'NONE': 0, 'PARTIAL': 1, 'COMPLETE': 2}
df['impact_availability'] = df['impact_availability'].map(impact_mapping)
df['impact_confidentiality'] = df['impact_confidentiality'].map(impact_mapping)
df['impact_integrity'] = df['impact_integrity'].map(impact_mapping)

# Correlation Matrix
correlation_matrix = df.corr()

# Heatmap Plot
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, cbar=True)

plt.title('Correlation Heatmap: CVSS Score vs CIA Impact')
plt.show()
