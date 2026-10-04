# Power BI Dashboard — RetailPulse

This directory contains the business intelligence reporting layer for the **RetailPulse** e-commerce analytics project.

---

## Directory Contents

* `README.md` — Dashboard documentation, data modeling design, and KPI specifications.
* `RetailPulse_Dashboard.pbix` — Place your active Power BI report file here upon creation.
* `screenshots/` — Visual exports and screenshots of report pages for portfolio presentation and reports.

---

## Recommended Report Architecture

### 1. Data Model Setup
- **Fact Table**: `transactions_cleaned`
- **Dimension Tables**: `customers_cleaned`, `products_cleaned`, `dim_date`
- **Schema**: Star Schema (One-to-Many relationships from Dimensions to Fact table).

### 2. Suggested Report Pages
1. **Executive Overview**: High-level KPIs (Total Revenue, Orders, AOV, Gross Margin %, Return Rate, MoM growth).
2. **Sales & Category Performance**: Sales trends over time, top performing brands/categories, basket analysis.
3. **Customer Segmentation & RFM**: Customer tiers, acquisition channel effectiveness, repeat purchase rates, geographical distribution.
4. **Operations & Fulfillment**: Delivery timelines, carrier/shipping performance, return rate analysis by product and region.

---

## Exporting Screenshots
Save high-resolution screenshots of each dashboard page to `dashboards/powerbi/screenshots/` and embed them into `reports/final_project_report.md`.
