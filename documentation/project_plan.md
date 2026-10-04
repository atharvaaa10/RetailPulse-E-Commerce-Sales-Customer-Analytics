# RetailPulse — Project Execution Plan

## 1. Project Goal
Transform raw, messy e-commerce data into business-ready insights and executive dashboards while developing comprehensive, industry-grade Data Analyst competencies across Python, SQL, Statistics, and BI tools.

---

## 2. Project Phases & Milestones

### Phase 1: Environment & Project Inception
- [x] Repository and directory structure initialization
- [x] Environment requirements configuration (`requirements.txt`)
- [x] Schema reference and data dictionary establishment
- [ ] Environment validation (Python package installation)

### Phase 2: Data Understanding & Profiling
- [ ] **Notebook 01**: Data Understanding (domain grounding, schema inspection, dimension checking)
- [ ] **Notebook 02**: Data Profiling (uncovering nulls, duplicates, anomalies, type mismatches, out-of-range values)
- [ ] Log all identified quality issues in `documentation/data_cleaning_log.md`

### Phase 3: Data Cleaning & Preprocessing
- [ ] **Notebook 03**: Cleaning `transactions.csv`
- [ ] **Notebook 04**: Cleaning `customers.csv`
- [ ] **Notebook 05**: Cleaning `products.csv`
- [ ] Export validated datasets to `data/cleaned/`
- [ ] Document all cleaning actions and business rules in `reports/data_cleaning_report.md`

### Phase 4: Data Validation & Quality Assurance
- [ ] **Notebook 06**: Automated validation checks (PK uniqueness, referential integrity, domain bounds, dates)
- [ ] Sign off on clean dataset readiness

### Phase 5: Exploratory Data Analysis (EDA)
- [ ] **Notebook 07**: Sales EDA (revenue drivers, seasonal trends, channel dynamics)
- [ ] **Notebook 08**: Customer EDA (demographics, segmentation, cohort behavior)
- [ ] **Notebook 09**: Product EDA (catalog distribution, pricing elasticity, margin analysis)
- [ ] **Notebook 10**: Operations EDA (logistics, fulfillment SLAs, return analysis)
- [ ] Synthesize findings in `reports/exploratory_analysis_report.md`

### Phase 6: Statistical Analysis & Hypothesis Testing
- [ ] **Notebook 11**: Statistical analysis (distributions, parametric/non-parametric tests, correlation vs causation, ANOVA, Chi-Square)

### Phase 7: Data Visualization Mastery
- [ ] **Notebook 12**: Data storytelling and chart selection matrix (bar, line, box, heatmap, time-series)

### Phase 8: Strategic Insights & Business Synthesis
- [ ] **Notebook 13**: High-level business insight generation and actionable recommendations
- [ ] Draft `reports/business_insights_report.md`

### Phase 9: SQL Analysis & Modeling
- [ ] Execute scripts `01_basic_queries.sql` through `08_business_analysis.sql`
- [ ] Validate SQL outputs against Pandas EDA results

### Phase 10: Power BI Dashboard & Visual Delivery
- [ ] Build star-schema data model in Power BI Desktop
- [ ] Build interactive dashboards across Executive, Sales, Customers, and Operations views
- [ ] Capture screenshots in `dashboards/powerbi/screenshots/`

### Phase 11: Final Reporting & Portfolio Wrap-Up
- [ ] Finalize `reports/final_project_report.md`
- [ ] Document takeaways in `documentation/lessons_learned.md`
- [ ] Update main `README.md` completion badges and summary
