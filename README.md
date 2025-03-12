
# **CVE Analysis and Reporting System**

## **Introduction**
The CVE Analysis and Reporting System is designed to analyze cybersecurity vulnerability data by parsing, visualizing, and reporting key insights. This system leverages the CVSS scoring framework, CWE classifications, and data-driven analysis to identify trends, categorize security weaknesses, and support vulnerability management decisions.

This project was developed to improve vulnerability insights by analyzing CVE data efficiently, visualizing trends, and categorizing security risks for better decision-making. By leveraging data science tools such as Pandas and Matplotlib, the system effectively identifies patterns in vulnerability data.

---

## **Project Objectives**
The primary objectives of this project are to:
- Load and clean CVE data efficiently.
- Categorize CVEs using the CVSS scoring system.
- Extract insights into CWE trends and vulnerability patterns.
- Visualize attack vectors, confidentiality impacts, and vendor distribution.
- Provide actionable insights by visualizing CVEs reported over time.

---

## **Dataset Overview**

This dataset contains detailed information about security vulnerabilities, including metadata, impact, and access information. Below is a description of the dataset's columns:

| #  | Column Name             | Non-Null Count | Data Type |
|----|-------------------------|-----------------|------------|
| 0  | `Unnamed: 0`             | 89660           | `object`    |
| 1  | `mod_date`               | 89660           | `object`    |
| 2  | `pub_date`               | 89660           | `object`    |
| 3  | `cvss`                   | 89660           | `float64`   |
| 4  | `cwe_code`               | 89660           | `int64`     |
| 5  | `cwe_name`               | 89660           | `object`    |
| 6  | `summary`                | 89660           | `object`    |
| 7  | `access_authentication`  | 88776           | `object`    |
| 8  | `access_complexity`      | 88776           | `object`    |
| 9  | `access_vector`          | 88776           | `object`    |
| 10 | `impact_availability`    | 88776           | `object`    |
| 11 | `impact_confidentiality` | 88776           | `object`    |
| 12 | `impact_integrity`       | 88776           | `object`    |

## Column Descriptions
- **`Unnamed: 0`**: Likely an index column or identifier with no specific meaning.
- **`mod_date`**: The date the entry was last modified.
- **`pub_date`**: The publication date of the vulnerability entry.
- **`cvss`**: The Common Vulnerability Scoring System (CVSS) score for the vulnerability.
- **`cwe_code`**: The CWE (Common Weakness Enumeration) code identifying the type of vulnerability.
- **`cwe_name`**: The name corresponding to the CWE code.
- **`summary`**: A brief description of the vulnerability.
- **`access_authentication`**: Details about the authentication requirements for exploiting the vulnerability.
- **`access_complexity`**: The complexity involved in exploiting the vulnerability.
- **`access_vector`**: The vector through which the vulnerability can be exploited (e.g., network, local).
- **`impact_availability`**: Impact on the system’s availability if exploited.
- **`impact_confidentiality`**: Impact on the system’s confidentiality if exploited.
- **`impact_integrity`**: Impact on the system’s integrity if exploited.

---

## **Project Structure**

- **`main.py`** - Main application logic that coordinates data loading, analysis, and reporting.
- **`dataset_loader.py`** - Loads and prepares CVE data from CSV files.
- **`cvss_categoriser.py`** - Categorizes CVEs based on CVSS scoring criteria.
- **`cwe_parser.py`** - Parses CWE codes for trend analysis.
- **`cve_parser.py`** - Tracks CVEs per year to understand reporting trends.
- **`vendors_parser.py`** - Analyzes vendor-specific data for vulnerability tracking.
- **`/archive`** - Contains CSV files such as:
  - `cve.csv` - CVE data entries.
  - `products.csv` - Product details.
  - `vendor_product.csv` - Vendor-product mapping.
  - `vendors.csv` - Vendor information.

---

## **How to Run the Project**
1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/your-repository
   cd analysis-report
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas matplotlib numpy statsmodels scipy pymc
   ```

3. Run the main application:
   ```bash
   python main.py
   ```

4. The analysis results, including visualizations and insights, will be saved in the `/figures` directory.
