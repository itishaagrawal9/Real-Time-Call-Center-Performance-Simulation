# Real-Time Call Center Performance Simulation Dashboard 
End-to-end call center analytics project simulating real-time operations with Python automation, SQL Server data pipeline, and Power BI dashboards for performance monitoring and insights.

## Overview 
This project simulates a real-world call center environment by generating live call data using Python and visualizing it through an interactive Power BI dashboard.


![image_alt](https://github.com/itishaagrawal9/Real-Time-Call-Center-Performance-Simulation/blob/60b619f9adb89ae1f66d63359f591cedd8aa506f/Dashboard_Call%20Center_Simulation.png?raw=true)

## Tech Stack 
* Python (Data Simulation)
* SQL Server (SSMS)
* Power BI (Dashboard & Visualization)
* DAX (Measures & KPIs)

## Data Pipeline
Python Script → SQL Server → Power BI → Real-Time Dashboard

## Key Features
* Real-time call data simulation
* Automated data ingestion into SQL Server
* Interactive Power BI dashboard with live updates
* KPI tracking: response time, call duration, ratings, complaints
* Geo-analysis of call distribution
* Agent performance monitoring

## Dashboard Highlights
* Avg Agent Rating Gauge
* Complaint Distribution
* Call Trends Over Time
* Location-Based Insights
* Issue-Level Analysis

## Data Model
* Fact Table: Calls
* Dimension Tables: Agents (CSRs), Issues, Locations, Status, Companies

## How to Run
1. Run Python script to generate data
2. Load data into SQL Server
3. Connect Power BI to SQL Server
4. Enable auto-refresh
