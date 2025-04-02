import matplotlib.pyplot as plt
import numpy as np

# Sample Data
cwe_categories = ['CWE-352', 'CWE-79', 'CWE-89', 'CWE-200', 'CWE-269']
impact_availability = [20, 35, 30, 35, 27]
impact_confidentiality = [25, 32, 34, 20, 25]
impact_integrity = [15, 30, 20, 40, 20]

x = np.arange(len(cwe_categories))  # Bar positions
width = 0.35  # Bar width

# Creating Stacked Bars
plt.figure(figsize=(10, 6))
plt.bar(x, impact_availability, width, label='Availability Impact', color='#1f77b4')
plt.bar(x, impact_confidentiality, width, bottom=impact_availability, label='Confidentiality Impact', color='#ff7f0e')
plt.bar(x, impact_integrity, width, bottom=np.array(impact_availability) + np.array(impact_confidentiality), label='Integrity Impact', color='#2ca02c')

# Customizing the Chart
plt.xlabel('CWE Categories')
plt.ylabel('Number of CVEs')
plt.title('Impact Analysis by CWE Categories')
plt.xticks(x, cwe_categories)
plt.legend()

plt.tight_layout()
plt.show()