import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate cwe statistics
def access_complexity_statistics(cve):
    # Count the number of occurrences for each access complexity type
    access_complexity_count = cve['access_complexity'].value_counts().reset_index()
    access_complexity_count.columns = ['access_complexity', 'Count']

    # Display results
    print(access_complexity_count)

    # draw the figure and save it in figures folder
    # Define colors for the pie chart, I will be using the same colors as in the other figures
    # navy blue, steel blue, light gray
    colors = ['#4D648D', '#9FB1BC', '#E6E6E6']

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.pie(access_complexity_count['Count'], 
            labels=access_complexity_count['access_complexity'], autopct='%1.1f%%',
            startangle=140, colors=colors)
    plt.title('Access Complexity Distribution')

    # Save and display the chart
    plt.tight_layout()
    plt.savefig('./figures/access_complexity.png', dpi=600, transparent=True)
    plt.show()

    return access_complexity_count