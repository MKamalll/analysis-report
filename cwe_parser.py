import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate cwe statistics
def cwes_statistics(cve):
    cwes_count = cve['cwe_code'].value_counts().reset_index()
    cwes_count.columns = ['cwe_code', 'Count']

    # Take top 10
    top_10 = cwes_count.head(10).copy()

    # Map each cwe_code to its name by looking up the first corresponding name in the cve table
    cwe_names = []
    for code in top_10['cwe_code']:
        name = cve[cve['cwe_code'] == code]['cwe_name'].unique()
        cwe_names.append(name[0] if len(name) > 0 else 'Unknown')

    top_10['cwe_name'] = cwe_names

    # Display results
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(top_10)
    return cwes_count

# Function to display CWE data
def cwes_show(cwes_count):
    """ Draw the figure and save it in the 'figures' folder """
    
    # Ensure only top 5 CWEs are plotted
    top_10_cwes = cwes_count.nlargest(10, 'Count')
    plt.figure(figsize=(8, 5))
    cwe_labels = top_10_cwes['cwe_code'].astype(str).apply(lambda x: f"CWE-{x}")
    plt.bar(cwe_labels,
            top_10_cwes['Count'], 
            color='darkblue')

    plt.title('Top 10 Most Affected CWEs')
    plt.xlabel('CWE Code')
    plt.ylabel('Number of CWEs')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=45, ha='right')

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/top_10_cwes.png', dpi=300, transparent=True)

    # Display the chart
    plt.show()