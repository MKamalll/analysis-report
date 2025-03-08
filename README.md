# Dataset Overview

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

## Notes
- The dataset contains **89660** entries.
- Some columns have a slightly lower count (e.g., `access_authentication`, `access_complexity`, etc.), indicating missing values.

This dataset is ideal for vulnerability detection, patching analysis, and security impact assessments.


# **CVE Analysis and Reporting System**

## **Project Structure**

# Project Structure

- `/analysis-report`
  - `main.py` - Main application logic
  - `data_loader.py` - CSV file loader
  - `cvss_categorizer.py` - CVSS categorization logic
  - `/archive`
    - `cve.csv` - CVE data
    - `products.csv` - Product information
    - `vendor_product.csv` - Vendor-product mapping
    - `vendors.csv` - Vendor details

## **Description of Project Components**

### **1. `main.py`**
> **The main entry point of the application.**  
- Contains the `main()` function that orchestrates the entire analysis workflow.
- Imports functions from `data_loader.py` and `cvss_categorizer.py`.
- Handles:
  - Data loading
  - CVSS categorization
  - Visualization of results
  - Reporting
- Includes a `printCVE()` function to display key dataset insights such as:
  - Dataset information
  - Column details
  - Sample records

---

### **2. `data_loader.py`**
> **Handles dataset loading and preparation.**  
- Defines the `load_data()` function, which loads:
  - **`cve.csv`**: Contains vulnerability data with CVSS scores.
  - **`products.csv`**: Contains product-related information.
  - **`vendor_product.csv`**: Links vendors to their products.
  - **`vendors.csv`**: Contains vendor details.
- Ensures proper data loading to prevent file path errors.

---

### **3. `cvss_categorizer.py`**
> **Responsible for CVSS score categorization.**  
- Defines the `categorize_cvss()` function to classify CVSS scores into:
  - **Critical** (≥ 9.0)
  - **High** (7.0 – 8.9)
  - **Medium** (4.0 – 6.9)
  - **Low** (1.0 – 3.9)
  - **None** (< 1.0)
- Provides the `add_cvss_category()` function, which applies this classification to the CVE dataset.

---

### **4. `/archive/` (Data Directory)**
> **Contains the CSV data files used in the analysis.**

- **`cve.csv`**: Main dataset with CVSS scores, vulnerability details, and impact data.
- **`products.csv`**: Contains information on affected software and hardware.
- **`vendor_product.csv`**: Establishes relationships between vendors and their products.
- **`vendors.csv`**: Details about the vendors providing the affected products.

---

## **How to Run the Project**
1. Clone the repository or create the folder structure as shown.
2. Install the required dependencies by running:
   ```bash
   pip install pandas matplotlib numpy statsmodels scipy pymc
    ```
3. Run the main.py file:
   ```bash
   python main.py
   ```