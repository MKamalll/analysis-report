import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate cwe statistics
def cwes_statistics(cve):
    cwes_count = cve['cwe_code'].value_counts().reset_index(name='Count')
    cwes_count.columns = ['cwe_code', 'Count']

    # Display results
    print(cwes_count)
    return cwes_count

# Function to display CWE data
def cwes_show(cwes_count):
    """ Draw the figure and save it in the 'figures' folder """
    
    # Ensure only top 5 CWEs are plotted
    top_5_cwes = cwes_count.nlargest(5, 'Count')
    plt.figure(figsize=(8, 5))
    plt.bar(top_5_cwes['cwe_code'].astype(str),  # Ensure CWE codes are treated as categorical
            top_5_cwes['Count'], 
            color=['red', 'orange', 'yellow', 'green', 'gray'])

    plt.title('Top 5 Most Affected CWEs')
    plt.xlabel('CWE Code')
    plt.ylabel('Number of CWEs')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  # Improved readability
    plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/top_5_cwes.png', dpi=300, transparent=True)

    # Display the chart
    plt.show()