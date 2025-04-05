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
    # Parse and visualize the 'access_vector' data from CVE dataset.
    
    # Count the number of occurrences for each attack vector
    attack_vector_count = cve_data['access_vector'].value_counts().reset_index()
    attack_vector_count.columns = ['access_vector', 'Count']

    # Display results
    print(attack_vector_count)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.pie(attack_vector_count['Count'], 
            labels=attack_vector_count['access_vector'], autopct='%1.1f%%',
            startangle=140)
    plt.title('Attack Vector Distribution')

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
        plt.savefig(f'./figures/{impact}_impact_distribution.png', dpi=300, transparent=True)
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
             linestyle='-', color='darkblue')

    plt.title('CVEs Over Time')
    plt.xlabel('Years')
    plt.ylabel('Number of CVEs')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  
    plt.xticks(rotation=45, ha='right')

    # Save the figure
    plt.tight_layout()
    plt.savefig('./figures/cves_over_time.png', dpi=300, transparent=True)

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
    df.columns = df.columns.droplevel(1)  # Flatten multi-index
    df = df.reindex(['NONE', 'PARTIAL', 'COMPLETE'])

    # Bar plot setup
    x = np.arange(len(df.index))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar(x - width, df['impact_confidentiality'], width, label='Confidentiality', color='#a6bddb')
    plt.bar(x, df['impact_integrity'], width, label='Integrity', color='#3690c0')
    plt.bar(x + width, df['impact_availability'], width, label='Availability', color='#0570b0')

    plt.xlabel('Impact Level')
    plt.ylabel('Count')
    plt.title('Impact Level Distribution Across Dimensions')
    plt.xticks(x, df.index)
    plt.legend(title='Impact Type')
    plt.tight_layout()
    plt.savefig('./figures/impact_level_distribution_grouped.png', dpi=300, transparent=True)
    plt.show()


def vulnerable_product_parser_top3(products_data):
    # Ensure column names are stripped and in lowercase
    print(products_data.columns)
    print(products_data.head(10)) 
    products_data.columns = products_data.columns.str.strip().str.lower()
    
    # Extract year from CVE ID (e.g., 'CVE-2019-12345' → 2019)
    products_data['year'] = products_data['cve_id'].str.extract(r'CVE-(\d{4})')[0].astype(int)

    # Filter to include only the last 5 years
    products_data = products_data[products_data['year'] >= (products_data['year'].max() - 4)]

    # Count occurrences of each product per year
    grouped = products_data.groupby(['year', 'vulnerable_product']).size().reset_index(name='Count')

    # Get top 3 products per year
    top3_per_year = grouped.groupby('year').apply(lambda x: x.nlargest(3, 'Count')).reset_index(drop=True)

    # Pivot for plotting
    pivot_df = top3_per_year.pivot(index='vulnerable_product', columns='year', values='Count').fillna(0)

    # Plot
    pivot_df.T.plot(kind='bar', figsize=(12, 6), width=0.7)
    plt.xlabel('Year')
    plt.ylabel('Number of Vulnerabilities')
    plt.title('Top 3 Vulnerable Products Per Year')
    plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('./figures/top_3_vulnerable_products_per_year.png', dpi=300, transparent=True)
    plt.show()

    return top3_per_year


def vulnerable_product_parser(products_data):
    # Ensure column names are stripped and in lowercase
    products_data.columns = products_data.columns.str.strip().str.lower()

    # Count total CVEs per product
    product_counts = products_data['vulnerable_product'].value_counts().nlargest(10).reset_index()
    product_counts.columns = ['Product', 'CVE Count']

    # Plot horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(product_counts['Product'], product_counts['CVE Count'], color='blue')
    plt.xlabel('Number of CVEs')
    plt.ylabel('Product')
    plt.title('Top 10 Most Affected Products')
    plt.gca().invert_yaxis()  # Highest value at the top
    plt.tight_layout()
    plt.savefig('./figures/top_10_vulnerable_products.png', dpi=300, transparent=True)
    plt.show()

    return product_counts