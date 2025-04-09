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

# def fun Dynamically parse, count, and visualize impact data
def impact_parse(cve_data):    
    # List of impact categories
    impact_columns = [
        'impact_confidentiality',
        'impact_integrity',
        'impact_availability'
    ]

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
        #colors = ['orange', 'lightblue', 'blue']
        plt.figure(figsize=(8, 5))
        plt.pie(impact_counts['Count'], 
                labels=impact_counts[impact], 
                autopct='%1.1f%%', 
                startangle=140)

        plt.title(f'{impact} Impact Distribution')
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        # Save and display the chart
        plt.tight_layout()
        plt.savefig(f'./figures/{impact}_impact_distribution.png', dpi=600, transparent=True)
        plt.show()

    return impact_data

# Function to display CWE data
def cves_show(cves_per_year):
# Draw the figure and save it in the 'figures' folder
    
    # Ensure only top 10 years are plotted
    cves_over_time = cves_per_year.sort_values(by='year', ascending=True).tail(21)

    plt.figure(figsize=(8, 5))
    plt.plot(cves_over_time['year'].astype(str), 
             cves_over_time['Count'], 
             linestyle='-', color='#0570b0')

    plt.title('CVEs Over Time')
    plt.xlabel('Years')
    plt.ylabel('Number of CVEs')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  
    plt.xticks(rotation=45, ha='right')

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/cves_over_time.png', dpi=600, transparent=True)

    # Display the chart
    plt.show()

def impact_parse_grouped(cve_data):
    # Draw a grouped bar chart comparing impact levels across dimensions

    import numpy as np

    # List of impact categories
    impact_columns = [
        'impact_confidentiality',
        'impact_integrity',
        'impact_availability'
    ]

    # Dictionary to store parsed data
    impact_data = {}

    for impact in impact_columns:
        impact_counts = cve_data[impact].value_counts().reset_index()
        impact_counts.columns = ['Impact Level', 'Count']
        impact_counts.set_index('Impact Level', inplace=True)
        impact_data[impact] = impact_counts

    # Create a combined DataFrame
    df = pd.concat(impact_data, axis=1)
    df.columns = df.columns.droplevel(1)
    df = df.reindex(['NONE', 'PARTIAL', 'COMPLETE'])

    # Bar plot setup
    x = np.arange(len(df.index))
    width = 0.25

    plt.figure(figsize=(10, 6))

    # I will choose this color scheme for the bars #a6bddb , #3690c0 , #0570b0
    # colors are grades of blue
    plt.bar(x - width, df['impact_confidentiality'], width, label='Confidentiality', color='#a6bddb')
    plt.bar(x, df['impact_integrity'], width, label='Integrity', color='#3690c0')
    plt.bar(x + width, df['impact_availability'], width, label='Availability', color='#0570b0')

    plt.xlabel('Impact Level')
    plt.ylabel('Count')
    plt.title('Impact Level Distribution Across Dimensions')
    plt.xticks(x, df.index)
    plt.legend(title='Impact Type')
    plt.tight_layout()
    plt.savefig('./figures/impact_level_distribution_grouped.png', dpi=600, transparent=True)
    plt.show()


def vulnerable_product_parser(products_data):
    # Ensure column names are stripped and in lowercase
    products_data.columns = products_data.columns.str.strip().str.lower()

    # Count total CVEs per product
    product_counts = products_data['vulnerable_product'].value_counts().nlargest(10).reset_index()
    product_counts.columns = ['Product', 'CVE Count']

    # Plot horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(product_counts['Product'], product_counts['CVE Count'], color='#0570b0')
    plt.xlabel('Number of CVEs')
    plt.ylabel('Product')
    plt.title('Top 10 Most Affected Products')
    plt.gca().invert_yaxis()  # Highest value at the top
    plt.tight_layout()
    plt.savefig('./figures/top_10_vulnerable_products.png', dpi=600, transparent=True)
    plt.show()

    return product_counts