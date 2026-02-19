# E-commerce Analytics & BI Dashboard

This repository contains a **production-style end-to-end Business Intelligence solution** for an e-commerce environment, integrating **sales, customer, product, and marketing data** into a unified analytical model. The project emphasizes **data modeling, metric definition, and decision-oriented analytics**, rather than visualization alone.

## Objetive

The objective of this project is to design a **comprehensive BI solution** that enables business stakeholders to: 
- Monitor commercial performance at an executive level
- Understand customer behavior and purchasing patterns
- Evaluate product performance and return dynamics
- Assess marketing efficiency through Cost per Conversion and other conversion metrics

## Data Sources

The analysis is based on **synthetic datasets** representing core e-commerce business domains: - **Sales & Orders**: customers, orders, order items, product returns 
- **Products**: product catalog and inventory
- **Marketing**: campaigns, performance metrics, and email marketing logs

The datasets are designed to reflect **real-world analytical complexity**, including multiple fact tables, shared dimensions, and differing analytical grains.

## Data Preparation & Transformation

Raw data was **pre-processed using Python scripts** before being loaded into Power BI. 

Key transformation decisions included:
- Standardization of data types and date fields
- Creation of clean dimension tables for customers, products, and campaigns
- Alignment of analytical grain across fact tables to ensure reliable aggregation

Transformations were intentionally kept **close to the reporting layer** to prioritize transparency, traceability, and fast iteration. 

> In a production environment, these transformations would typically be migrated upstream (e.g., SQL / dbt) to improve scalability, performance, and governance.

## Data Model & Design Choices

The semantic model follows a **star-schema / constellation approach**, clearly separating:
- **Fact tables**: orders, order items, conversions, campaign performance
- **Dimension tables**: customers, products, campaigns, dates

Key design principles:
- Clear grain definition per fact table
- Single-direction filtering to avoid ambiguity
- Explicit metric definitions to ensure consistency across reports

This structure supports **performance, analytical clarity, and long-term extensibility**.

## Metrics & Business Logic

Key Business metrics implemented using DAX include:
- **Revenue** – Aggregated from completed orders
- **Average Order Value (AOV)** – Revenue / Orders
- **Customer Order Frequency** – Orders per customer
- **Return Rate** – Returned items / sold items
- **Conversion Rate** – Conversions / Sessions
- **Cost per Conversion** – Marketing spend / Conversions

Cost per Conversion indicates the average marketing cost required to generate a conversion, helping skateholders evaluate campaign efficiency.

## Dashboard Structure

### Executive Overview
- Revenue, Orders, Customers, AOV
- Revenue and order trends over time
- Customer segmentation analysis

![Executive Overview](screenshots/Executive Overview.png)

### Customer Analysis
- New vs Returning Customers
- Order frequency distribution
- Revenue contribution by customer segment

### Product Performance
- Revenue by product category
- Top products by revenue
- Return rate by product category

### Marketing Performance
- Campaign cost and conversion trends
- Cost per Conversion
- Campaign-level efficiency indicators

Each page is designed to answer specific business questions, avoiding metric duplication and visual clutter.

## Tools & Technologies

- **Power BI** - Data modeling, DAX, interactive dashboards
- **Python** – Data preparation and transformation
- **Excel** – Synthetic raw data sources

## Key Takeaways

- Strong focus on **analytical modeling over visual complexity**
- Business-driven metric definitions with clear assumptions
- Scalable data model aligned with BI best practices
- Dashboard designed to support **decision-making, not static reporting**
