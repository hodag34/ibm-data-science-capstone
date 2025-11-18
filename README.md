IBM Applied Data Science Capstone
Predicting Falcon 9 First Stage Landing Outcomes Using Machine Learning

This repository contains all project assets for the IBM Applied Data Science Capstone. The goal of the project is to use real SpaceX launch data to predict whether a Falcon 9 first-stage booster will successfully land. The project integrates multiple data science techniques, including data collection, data wrangling, exploratory analysis, interactive visualization, and predictive modeling.

Repository Contents
1. Data Collection

• jupyter-labs-spacex-data-collection-api.ipynb
 Collects launch records using the SpaceX REST API
• jupyter-labs-webscraping.ipynb
 Scrapes historical launch data from Wikipedia

2. Data Wrangling & Preprocessing

• labs-jupyter-spacex-Data wrangling.ipynb
 Cleans data, handles missing values, merges datasets, prepares features

3. Exploratory Data Analysis (EDA)

• edadataviz.ipynb
 Visualization-based EDA using Matplotlib and Seaborn
• jupyter-labs-eda-sql-coursera_sqllite.ipynb
 SQL-based EDA using SQLite queries

4. Interactive Visual Analytics

• lab_jupyter_launch_site_location.ipynb
 Folium map showing launch site locations, outcomes, and proximities
• spacex-dash-app.py
 Interactive Plotly Dash dashboard for mission success analysis
• spacex_launch_dash.csv
 Dataset used by the Dash application

5. Machine Learning: Predictive Analysis

• SpaceX_Machine Learning Prediction_Part_5.ipynb
 Builds and evaluates classification models (LR, SVM, KNN, Decision Tree)
 Decision Tree achieved the highest accuracy

6. Data Files

• spacex_web_scraped.csv
• dataset_part_2.csv
• Additional intermediate files used throughout the analysis

Project Overview

This project answers the key question:
“Can we predict the success of a Falcon 9 first-stage landing?”

Work completed includes:

• Collecting mission data via API and web scraping
• Wrangling and merging datasets
• EDA via visualization and SQL queries
• Folium map visualizations of launch locations and outcomes
• Interactive Plotly Dash dashboard for payload and site-based performance
• Training and comparing multiple machine learning models
• Evaluating the best classifier using accuracy and a confusion matrix

Final Deliverables

• Full 65-page final PDF presentation
• Complete GitHub repository with all notebooks, data, visuals, and app code
• Predictive model identifying most important features influencing landing success
