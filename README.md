# PhonePe-Data-Visualization
Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

# Problem Statement:
The Phonepe pulse Github repository contains data related to various metrics and statistics.The goal is to extract this data and process it to obtain insights and information that can be visualized.

# Data:
https://github.com/PhonePe/pulse?tab=readme-ov-file#phonepe-pulse---data
Aggregated : Aggregated values of various payment categories as shown under Categories section
Map : Total values at the State and District levels
Top : Totals of top States / Districts / Postal Codes

# Approach: 
**1)Data extraction:** Clone Phonepe pulse Github repository using scripting to fetch the data and store as JSON
**2)Data transformation:** Pre-process the data ,transform into a format suitable for analysis and visualization.
**3)Database insertion:** Use "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
**4)Dashboard creation:** Use Streamlit and Plotly libraries to create an interactive dashboard. Plotly's built-in geo map functions used to display the data on a map and Streamlit used to create a user-friendly interface with necessary dropdown options.
**5)Data retrieval:** Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically. 
**6)Deployment:** Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard.

# Results:
A live geo visualization interactive dashboard that displays insights from the Phonepe pulse Github repository making it a valuable tool for data analysis and decision-making. 
The dashboard will have at least 10 different dropdown options for users to select different facts and figures to display. 
Data will be stored in a MySQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data.
Users will be able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. 

