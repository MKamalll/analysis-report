import pandas as pd
import matplotlib.pyplot as plt

# Function to parse dates and count CVEs per year
def count_cves_per_year(cve_data):
    # Ensure 'pub_date' is in datetime format
    cve_data['pub_date'] = pd.to_datetime(cve_data['pub_date'], errors='coerce')

    # Extract the year from the 'pub_date'
    cve_data['year'] = cve_data['pub_date'].dt.year

    # Count CVEs per year
    cves_per_year = cve_data['year'].value_counts().reset_index()
    cves_per_year.columns = ['year', 'Count']

    # Sort by year for better visualization
    cves_per_year = cves_per_year.sort_values(by='year')

    # Display results
    print(cves_per_year)
    return cves_per_year

# Function to parse different attack vectors
def attack_vector_parse(cve_data):
    """Parse and visualize the 'access_vector' data from CVE dataset."""
    
    # Count the number of occurrences for each attack vector
    attack_vector_count = cve_data['access_vector'].value_counts().reset_index()
    attack_vector_count.columns = ['access_vector', 'Count']

    # Display results
    print(attack_vector_count)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.bar(attack_vector_count['access_vector'], attack_vector_count['Count'], 
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

    plt.title('Attack Vector Distribution')
    plt.xlabel('Access Vector')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Save and display the chart
    plt.tight_layout()
    plt.savefig('./figures/attack_vector.png', dpi=300, transparent=True)
    plt.show()

    return attack_vector_count

# def fun Dynamically parse, count, and visualize impact data
def impact_parse(cve_data):    
    # List of impact categories
    impact_columns = [
        'impact_confidentiality',
        'impact_integrity',
        'impact_availability'
    ]

    # Dictionary to store parsed data
    impact_data = {}

    # Loop through each impact category
    for impact in impact_columns:
        impact_counts = cve_data[impact].value_counts().reset_index()
        impact_counts.columns = [impact, 'Count']
        impact_data[impact] = impact_counts

        # Display results
        print(f"\n{impact} Impact Distribution:")
        print(impact_counts)

        # Plotting
        plt.figure(figsize=(8, 5))
        plt.bar(impact_counts[impact], impact_counts['Count'], 
                color=['#1f77b4', '#ff7f0e', '#2ca02c'])

        plt.title(f'{impact} Impact Distribution')
        plt.xlabel('Impact Level')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        # Save and display the chart
        plt.tight_layout()
        plt.savefig(f'./figures/{impact}_impact_distribution.png', dpi=300, transparent=True)
        plt.show()

    return impact_data

# Function to display CWE data
def cves_show(cves_per_year):
# Draw the figure and save it in the 'figures' folder
    
    # Ensure only top 10 years are plotted
    last_10_years_cves = cves_per_year.sort_values(by='year', ascending=True).tail(10)

    plt.figure(figsize=(8, 5))
    plt.plot(last_10_years_cves['year'].astype(str), 
             last_10_years_cves['Count'], 
             linestyle='-', color='black')

    plt.title('Top 5 Most Affected CWEs')
    plt.xlabel('Years')
    plt.ylabel('Number of CVEs')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  # Improved readability
    plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/last_10_years_cves.png', dpi=300, transparent=True)

    # Display the chart
    plt.show()