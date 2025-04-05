import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate cwe statistics
def access_authentication_statistics(cve):
    # Count the number of occurrences for each access authentication type
    access_authentication_count = cve['access_authentication'].value_counts().reset_index()
    access_authentication_count.columns = ['access_authentication', 'Count']

    # Display results
    print(access_authentication_count)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.pie(access_authentication_count['Count'], 
            labels=access_authentication_count['access_authentication'], autopct='%1.1f%%',
            startangle=140)
    plt.title('Access Authentication Distribution')

    # Save and display the chart
    plt.tight_layout()
    plt.savefig('./figures/access_authentication.png', dpi=300, transparent=True)
    plt.show()

    return access_authentication_count