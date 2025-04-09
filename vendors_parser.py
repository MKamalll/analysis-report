import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate vendor statistics
def vendors_statistics(vendors):
    vendors_count = vendors['vendor'].value_counts().reset_index(name='Count')
    vendors_count.columns = ['vendor', 'Count']

    # Display results
    print(vendors_count)
    return vendors_count

# Function to display vendor data
def vendors_show(vendors_count):
    #draw the figure and save it in figures folder
    # Ensure only top 10 vendors are plotted
    top_10_vendors = vendors_count.nlargest(10, 'Count')
    top_10_vendors = top_10_vendors.sort_values(by='Count')

    plt.figure(figsize=(8, 5))
    plt.barh(top_10_vendors['vendor'], top_10_vendors['Count'], 
             color=plt.cm.viridis_r(top_10_vendors['Count'] / top_10_vendors['Count'].max()))

    plt.title('Top 10 Most Affected Vendors')
    plt.xlabel('Number of CVEs')
    plt.ylabel('Vendor')
    plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/top_10_vendors.png', dpi=600, transparent=True)

    # Display the chart
    plt.show()
