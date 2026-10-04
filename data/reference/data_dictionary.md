# RetailPulse — Enterprise Data Dictionary

This reference document defines the standard schema, expected data types, and business semantics for all entities in the RetailPulse e-commerce data model.

---

## 1. Customers Dataset (`customers.csv`)

| Column | Description | Expected Type | Example | Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `Customer_ID` | Unique identifier for each customer | String (Alphanumeric) | `CUST-06877` | Primary key identifying individual registered shoppers |
| `Customer_Name` | Full name of the customer | String | `Mohit Iyer` | Contact and account identity of the customer |
| `Gender` | Gender identity of the customer | Categorical / String | `Male`, `Female` | Demographic dimension for customer profiling |
| `Age` | Age of the customer in years | Integer | `39` | Demographic indicator for segmenting cohorts |
| `City` | Customer's primary city of residence | String | `Chennai` | Geographic dimension for regional demand analysis |
| `State` | Customer's primary state of residence | String | `Tamil Nadu` | Regional administrative grouping for geographic reporting |
| `Customer_Segment` | Loyalty or lifecycle segment tier | Categorical / String | `Regular`, `New`, `VIP` | Behavioral classification for targeted marketing |
| `Registration_Date` | Date customer account was created | Date (`YYYY-MM-DD`) | `2023-11-12` | Timestamp marking cohort onboarding and customer vintage |
| `Acquisition_Channel` | Marketing channel through which customer joined | Categorical / String | `Paid Social`, `Email`, `Organic Search` | Origin channel evaluating marketing attribution and CAC |

---

## 2. Products Dataset (`products.csv`)

| Column | Description | Expected Type | Example | Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `Product_ID` | Unique identifier for each product SKU | String (Alphanumeric) | `PRD-0314` | Primary key identifying an individual catalog item |
| `Product_Name` | Descriptive name of the product SKU | String | `ITC Snacks Model-665` | Commercial display name of the product |
| `Category` | High-level product category | Categorical / String | `Grocery`, `Automotive`, `Electronics` | Top-level catalog classification for assortment analysis |
| `Subcategory` | Detailed product subcategory | Categorical / String | `Snacks`, `Car Accessories`, `Audio` | Granular product taxonomy grouping |
| `Brand` | Brand name or manufacturer | String | `ITC`, `Studds`, `Sony` | Brand identity used to evaluate brand partner performance |
| `Cost_Price` | Cost to acquire or manufacture the unit | Float / Numeric | `5452.67` | Unit inventory cost basis for gross margin calculation |
| `Listed_Price` | Recommended retail catalog price | Float / Numeric | `10289.84` | Benchmark retail price before promotional discounting |
| `Supplier` | Primary vendor or supplier supplying the SKU | String | `Supplier-Gamma-12` | Vendor partner responsible for sourcing and inventory supply |
| `Product_Rating` | Historical average customer rating for the SKU | Float (Scale: 1.0 - 5.0) | `3.4` | Historical catalog quality benchmark |

---

## 3. Transactions Dataset (`transactions.csv`)

| Column | Description | Expected Type | Example | Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `Order_ID` | Unique transaction order identifier | String (Alphanumeric) | `ORD-128400` | Primary key identifying an individual checkout transaction |
| `Order_Date` | Date transaction was placed | Date (`YYYY-MM-DD`) | `2025-12-20` | Transaction timestamp for sales trends and seasonality |
| `Customer_ID` | Identifier of customer placing order | String (Alphanumeric) | `CUST-10888` | Foreign key referencing `customers.Customer_ID` |
| `Product_ID` | Identifier of SKU purchased | String (Alphanumeric) | `PRD-0549` | Foreign key referencing `products.Product_ID` |
| `Quantity` | Number of units purchased | Integer | `3` | Volume of items ordered per line item |
| `Unit_Price` | Effective unit selling price at purchase | Float / Numeric | `21288.82` | Realized sales price per single unit |
| `Discount` | Promotional discount applied (percentage/ratio) | Float (0.0 to 1.0) | `0.15` | Discount concession applied to the line item |
| `Tax_Rate` | Applicable statutory tax rate (e.g., GST/VAT) | Float (0.0 to 1.0) | `0.18` | Tax obligation applicable to the transaction |
| `Shipping_Cost` | Shipping and handling fee charged | Float / Numeric | `0.00` | Freight revenue/charge levied for fulfillment |
| `Payment_Method` | Tender method used for checkout | Categorical / String | `COD`, `Credit Card`, `UPI` | Payment instrument utilized by the customer |
| `Order_Status` | Lifecycle status of order fulfillment | Categorical / String | `Delivered`, `Cancelled`, `Shipped` | Operational status of the transaction lifecycle |
| `Delivery_Days` | Elapsed transit duration from order to delivery | Float / Integer | `9` | Operational delivery turnaround time in calendar days |
| `Rating` | Customer review score for the order | Float / Integer (1 to 5) | `5` | Post-purchase customer satisfaction score |
| `Sales_Channel` | Platform / channel where order was booked | Categorical / String | `Web`, `Mobile App` | Digital sales touchpoint |
| `Coupon_Code` | Promotional coupon code applied | String | `FREESHIP` | Marketing campaign voucher code used at checkout |
| `Return_Flag` | Indicates if item was returned by customer | Categorical / Boolean | `Yes`, `No` | Reverse logistics and product return indicator |
