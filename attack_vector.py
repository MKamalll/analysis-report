import pandas as pd
import matplotlib.pyplot as plt

# Function to parse different attack vectors
def attack_vector_statistics(cve_data):
    # Parse and visualize the 'access_vector' data from CVE dataset.
    
    # Count the number of occurrences for each attack vector
    attack_vector_count = cve_data['access_vector'].value_counts().reset_index()
    attack_vector_count.columns = ['access_vector', 'Count']

    # Display results
    print(attack_vector_count)

    # Plotting
    plt.figure(figsize=(10, 8))
    plt.pie(attack_vector_count['Count'], 
            labels=attack_vector_count['access_vector'], autopct='%1.1f%%',
            startangle=140, textprops={'fontsize': 12})
    plt.title('Attack Vector Distribution')

    # Save and display the chart
    plt.tight_layout()
    plt.savefig('./figures/attack_vector.png', dpi=600, transparent=True)
    plt.show()

    return attack_vector_count