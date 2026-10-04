# RetailPulse — E-Commerce Sales & Customer Analytics

An end-to-end Data Analytics capstone project simulating the role of a Data Analyst at a fast-growing e-commerce company. This repository guides the complete data lifecycle: from raw messy data ingestion and profiling, through rigorous cleaning, validation, and exploratory analysis, to advanced statistical modeling, SQL querying, Power BI executive dashboards, and final commercial reporting.

---

## 1. Project Overview

RetailPulse represents a modern multi-category e-commerce platform operating across diverse product segments, customer demographics, and geographic regions. The project serves as an intensive, hands-on learning environment designed to build industry-standard competencies in data manipulation, business logic implementation, statistical inference, and data storytelling.

---

## 2. Business Problem

Leadership requires actionable, data-driven intelligence to address key commercial and operational challenges:
* **Revenue & Growth**: Identifying top-performing categories, brands, and products while understanding sales seasonality.
* **Profitability & Pricing**: Uncovering margin erosion caused by aggressive promotional discounting, high shipping absorption, and supplier cost variances.
* **Customer Dynamics & Churn**: Segmenting the customer base using RFM (Recency, Frequency, Monetary) modeling, cohort retention tracking, and acquisition channel evaluation.
* **Fulfillment & Logistics**: Diagnosing delivery bottlenecks, regional transit SLA breaches, and their direct impact on customer ratings and product returns.
* **Payment Systems**: Assessing payment method adoption, checkout preferences, and default/return risk profiles across channels.

---

## 3. Dataset Overview

The project models enterprise e-commerce operations across three relational domains (with full schema documentation in [`data/reference/data_dictionary.md`](data/reference/data_dictionary.md)):

* **Transactions (`data/raw/transactions.csv`)**: Transactional records capturing order identifiers, timestamps, customer references, product SKUs, pricing, discounts, tax rates, shipping costs, payment methods, delivery durations, review ratings, channels, and return indicators.
* **Customers (`data/raw/customers.csv`)**: Customer demographic master records including unique customer IDs, names, gender, age, geographic residence (city/state), loyalty segment tiers, registration dates, and acquisition channels.
* **Products (`data/raw/products.csv`)**: Catalog master dataset detailing product IDs, SKU names, product categories, subcategories, manufacturer brands, unit cost prices, list prices, primary suppliers, and benchmark catalog ratings.
* **Quality Reference (`data/hidden/data_quality_injection_log.csv`)**: Preserved reference log tracking injected data quality anomalies for post-cleaning audit and verification.

---

## 4. Project Objectives

1. **Python & Modern Analytics Tooling**: Master Pandas and NumPy for complex transformations, vectorized operations, and robust data wrangling.
2. **Data Understanding & Profiling**: Conduct structured audits to detect missing values, duplicates, mixed schemas, and hidden data corruptions.
3. **Data Cleaning & Standardization**: Remediate format inconsistencies, handle outliers systematically, and enforce enterprise business rules.
4. **Data Validation**: Construct automated, assertion-driven verification suites guaranteeing referential integrity and data hygiene.
5. **Exploratory Data Analysis (EDA)**: Execute deep univariate, bivariate, and multivariate analysis across sales, customers, catalog, and logistics.
6. **Inferential Statistics**: Apply hypothesis testing, ANOVA, confidence intervals, correlation matrices, and distribution evaluations.
7. **Visual Storytelling**: Develop purposeful, publication-grade data visualizations adhering to best practices in chart selection and cognitive load.
8. **Relational Database Modeling & SQL**: Author modular SQL scripts leveraging joins, aggregations, subqueries, CTEs, and window functions.
9. **Interactive Dashboarding**: Design and publish an executive Power BI report adhering to star-schema modeling principles.
10. **Executive Reporting**: Translate data findings into strategic business proposals, operational recommendations, and financial impact summaries.

---

## 5. Technology Stack

* **Programming & Manipulation**: Python 3.10+, Pandas, NumPy
* **Statistical Analysis**: SciPy, Statsmodels
* **Data Visualization**: Matplotlib, Seaborn
* **Database & Querying**: SQL (SQLite / PostgreSQL compatible), SQLAlchemy
* **Business Intelligence**: Microsoft Power BI Desktop
* **Notebook Environment**: Jupyter Notebooks
* **File & Data Handling**: OpenPyXL, Pathlib

---

## 6. Project Structure

```text
RetailPulse/
│
├── README.md                                  # Main project documentation & progress tracker
├── requirements.txt                           # Environment dependencies
├── .gitignore                                 # Git ignore configuration
│
├── data/
│   ├── raw/                                   # Immutable raw source datasets
│   │   ├── transactions.csv
│   │   ├── customers.csv
│   │   └── products.csv
│   ├── reference/                             # Data schema reference & data dictionary
│   │   └── data_dictionary.md
│   ├── cleaned/                               # Exported, clean datasets ready for downstream analysis
│   │   └── README.md
│   └── hidden/                                # Audit logs and reference anomaly records
│       └── data_quality_injection_log.csv
│
├── notebooks/                                 # Guided, modular Jupyter notebooks
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_profiling.ipynb
│   ├── 03_data_cleaning_transactions.ipynb
│   ├── 04_data_cleaning_customers.ipynb
│   ├── 05_data_cleaning_products.ipynb
│   ├── 06_data_validation.ipynb
│   ├── 07_eda_sales.ipynb
│   ├── 08_eda_customers.ipynb
│   ├── 09_eda_products.ipynb
│   ├── 10_eda_operations.ipynb
│   ├── 11_statistical_analysis.ipynb
│   ├── 12_visualization.ipynb
│   └── 13_business_insights.ipynb
│
├── sql/                                       # Progressive SQL query exercises
│   ├── 01_basic_queries.sql
│   ├── 02_filtering_and_sorting.sql
│   ├── 03_aggregations.sql
│   ├── 04_joins.sql
│   ├── 05_subqueries.sql
│   ├── 06_ctes.sql
│   ├── 07_window_functions.sql
│   └── 08_business_analysis.sql
│
├── dashboards/
│   └── powerbi/                               # Power BI reports and screenshots
│       ├── README.md
│       └── screenshots/
│
├── reports/                                   # Structured executive and capstone reports
│   ├── data_cleaning_report.md
│   ├── exploratory_analysis_report.md
│   ├── business_insights_report.md
│   └── final_project_report.md
│
├── documentation/                             # Analyst tracking logs and research questions
│   ├── project_plan.md
│   ├── data_cleaning_log.md
│   ├── business_questions.md
│   └── lessons_learned.md
│
└── src/                                       # Reusable Python source code modules
    ├── __init__.py
    ├── data_loading.py
    ├── data_cleaning.py
    ├── data_validation.py
    └── analysis_utils.py
```

---

## 7. Learning Roadmap

1. **Step 1: Setup Environment**
   - Install dependencies: `pip install -r requirements.txt`
   - Review schema and entity relationships in [`data/reference/data_dictionary.md`](data/reference/data_dictionary.md).
2. **Step 2: Understand & Profile**
   - Work through [`notebooks/01_data_understanding.ipynb`](notebooks/01_data_understanding.ipynb) to inspect shapes, types, and raw sample records.
   - Profile the data systematically in [`notebooks/02_data_profiling.ipynb`](notebooks/02_data_profiling.ipynb) to identify nulls, duplicates, and anomalies.
   - Record discovered issues in [`documentation/data_cleaning_log.md`](documentation/data_cleaning_log.md).
3. **Step 3: Clean & Standardize**
   - Clean each entity separately in notebooks `03`, `04`, and `05`.
   - Export processed tables to `data/cleaned/`.
4. **Step 4: Automated Validation**
   - Run assertion suites in [`notebooks/06_data_validation.ipynb`](notebooks/06_data_validation.ipynb) to ensure zero schema violations.
5. **Step 5: Exploratory Data Analysis & Statistics**
   - Execute domain-specific EDA in notebooks `07`, `08`, `09`, and `10`.
   - Perform hypothesis testing and statistical evaluation in [`notebooks/11_statistical_analysis.ipynb`](notebooks/11_statistical_analysis.ipynb).
6. **Step 6: Visualization Mastery & Business Synthesis**
   - Complete chart justification and plotting in [`notebooks/12_visualization.ipynb`](notebooks/12_visualization.ipynb).
   - Formulate strategic recommendations in [`notebooks/13_business_insights.ipynb`](notebooks/13_business_insights.ipynb).
7. **Step 7: SQL Mastery & Power BI**
   - Practice SQL querying from fundamentals to window functions in [`sql/`](sql/).
   - Model and design interactive dashboards in [`dashboards/powerbi/`](dashboards/powerbi/).
8. **Step 8: Final Presentation**
   - Synthesize all findings into the final capstone report in [`reports/final_project_report.md`](reports/final_project_report.md).

---

## 8. Current Progress

Track your journey through each stage of the project:

* [ ] Data Understanding
* [ ] Data Profiling
* [ ] Data Cleaning
* [ ] Data Validation
* [ ] EDA
* [ ] Statistics
* [ ] Visualization
* [ ] Business Insights
* [ ] SQL Analysis
* [ ] Power BI Dashboard
* [ ] Final Report
