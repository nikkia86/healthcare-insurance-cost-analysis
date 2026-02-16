Healthcare Insurance Cost Analysis – Advanced Data Analytics Capstone
Project Overview

This project presents an end to end data analytics solution analysing healthcare insurance costs using statistical analysis, hypothesis testing, and supervised machine learning. The objective is to understand how personal attributes such as age, BMI, smoking status, number of children, and region influence medical insurance charges.

The project integrates Python based exploratory data analysis with an interactive Streamlit dashboard and is deployed using Heroku.

Dataset

Healthcare Insurance Dataset
Authors: Willian Oliveira and Arun Jangir
Source: https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance

The dataset contains demographic and lifestyle attributes alongside insurance charges. These variables are used to investigate cost drivers and build a predictive model.

Business Objective

The primary analytical objective is to:

Identify factors that significantly influence healthcare insurance charges

Statistically test whether smokers incur higher insurance costs

Build a predictive model to estimate insurance charges

Deliver an interactive dashboard for stakeholders

ETL Pipeline

An Extract, Transform, Load approach was implemented:

Extract

The dataset was loaded from a CSV file using pandas.

Transform

Data preprocessing included:

Checking for missing values

Encoding categorical variables using one hot encoding

Preparing feature variables for modelling

Load

The cleaned and transformed dataset was stored in memory for analysis and modelling.

Exploratory Data Analysis

Descriptive statistical analysis was conducted using:

Mean

Median

Standard deviation

Distribution plots

Correlation analysis

Grouped comparisons

Key findings include:

Insurance charges are positively skewed

Smokers incur significantly higher average costs

Age and BMI show moderate positive relationships with charges

Hypothesis Testing

A two sample t test was conducted to compare insurance charges between smokers and non smokers.

The results demonstrated a statistically significant difference in mean charges between the two groups, supporting the hypothesis that smoking status impacts insurance costs.

Machine Learning Implementation

A supervised machine learning approach was applied using Linear Regression from scikit-learn.

Steps included:

Feature and target variable definition

Train test split

Model training

Model evaluation

Saving the trained model using joblib

Evaluation metrics included:

Mean Absolute Error

Mean Squared Error

Root Mean Squared Error

R² Score

The model demonstrates strong predictive capability in estimating insurance charges based on demographic and behavioural attributes.

This supervised implementation satisfies the requirement to apply an appropriate predictive algorithm to address a defined analytical problem.

Dashboard Implementation

An interactive Streamlit dashboard was developed to:

Visualise insurance charge distributions

Display smoker vs non smoker comparisons

Present correlation insights

Provide interactive filtering

Deliver dynamic visualisations using Plotly and Seaborn

The dashboard enables stakeholders to explore insurance cost drivers in a user friendly interface.

Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Plotly

Scikit-learn

Joblib

Streamlit

Git and GitHub

Heroku

AI Usage Declaration

Generative AI tools including ChatGPT and GitHub Copilot were used as support tools throughout the project.

AI assistance was used for:

Concept clarification

Debugging support

Code refinement suggestions

Structuring documentation

Improving clarity of explanations

All modelling decisions, statistical interpretations, analytical reasoning, and final implementation choices were independently reviewed and validated to ensure academic integrity and alignment with project requirements.

Project Structure

Healthcare Insurance Cost Analysis
│
├── app.py
├── multi_page.py
├── dashboard.py
├── models/
│ └── insurance_model.pkl
├── Jupyter_Notebooks/
│ └── 01_ExploratoryDataAnalysis.ipynb
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md

Deployment

The project is deployed using Heroku.

To run locally:

streamlit run app.py

Reflection

This project strengthened understanding of:

Statistical inference

Hypothesis testing

Supervised machine learning

Model evaluation

Dashboard development

Deployment workflows

It provided practical experience integrating analytics tools into a structured, professional data application.