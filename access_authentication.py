import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate cwe statistics
def access_authentication_statistics(cve):
    # Count the number of occurrences for each access authentication type
    access_authentication_count = cve['access_authentication'].value_counts().reset_index()
    access_authentication_count.columns = ['access_authentication', 'Count']

    # Display results
    print(access_authentication_count)

    # draw the figure and save it in figures folder
    # Define colors for the pie chart, I will be using the same colors as in the other figures
    # navy blue, steel blue, light gray
    colors = ['#4D648D', '#9FB1BC', '#E6E6E6']

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.pie(access_authentication_count['Count'], 
            labels=access_authentication_count['access_authentication'], autopct='%1.1f%%',
            startangle=140,colors=colors)
    plt.title('Access Authentication Distribution')

    # Save and display the chart
    plt.tight_layout()
    plt.savefig('./figures/access_authentication.png', dpi=600, transparent=True)
    plt.show()

    return access_authentication_count