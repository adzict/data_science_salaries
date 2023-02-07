# Data Science Salaries Streamlit App
![project_header](https://github.com/adzict/data_science_salaries/blob/main/assets/handshake_banner_1.jpg)

## Table of Contents

1. [ Project Introduction ](#Project_Introduction)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Methods Used ](#Methods_Used)
4. [ Project Description ](#Project_Description)
   * [ 1. Data Sources ](#Data_Sources)
   * [ 2. File Descriptions ](#File_Descriptions) 
5. [ Feature Notebooks and Deliverables ](#Notebooks_deliverables)
6. [ Acknowledgments ](#Acknowledgments)
7. [ Licences ](#Licences)
8. [ Contact ](#Contact)

## Project Introduction
<a name="Project_Introduction"></a>
<a name=""></a>

Before embarking on the journey of a job search, it is important to know current trends in the industry, as well as a salary range to be able to negotiate during your job hunt. This application will give you detailed insights of salary trends in the Data Science domain in the last 2 years. It is designed to help you understand how different factors, such as location, experience level, and employment type, impact salaries in the field.

## Technologies Used
<a name="Technologies_Used"></a>

* [Python](https://www.python.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Plotly](https://plotly.com/)
* [Streamlit](https://streamlit.io/)
* [Docker](https://www.docker.com/)

## Methods Used
<a name="Methods_Used"></a>

* Data Preprocessing / Data Cleaning
* Data Analysis
* Descriptive Statistics
* Feature Engineering
* Data Visualization
* Application Containerization
* Application Deployment
* Reporting


## Project Description
<a name="Project_Description"></a>


### Data Sources
<a name="Data_Sources"></a>

This dataset was aggregated from the ai-jobs.net Salaries, and can be obtained from the Kaggle website: [Data Science Job Salaries](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)

### File Descriptions
<a name="File_Descriptions"></a>

* [Data](https://github.com/adzict/data_science_salaries/tree/main/data) - folder containing processed data
* [Assets](https://github.com/adzict/data_science_salaries/tree/main/assets) - folder containing assets such as images
* [Data Science Salaries Dataset Exploration.ipynb](https://github.com/adzict/data_science_salaries/blob/main/Data%20Science%20Salaries%20Dataset%20Exploration.ipynb) - Notebook which contains the process of Basic Data Exploration and Preprocessing
* [main.py](https://github.com/adzict/data_science_salaries/blob/main/main.py) - Python script which deploys the model to Streamlit
* [requirements.txt](https://github.com/adzict/data_science_salaries/blob/main/requirements.txt) - a text files that contains all the dependencies needed to run the aplication on Streamlit


## Deliverables
<a name="Notebooks_deliverables"></a>

Access the application using the following link: [Data Science Salaries](https://adzict-data-science-salaries.streamlit.app/)

### Structure of the Notebook
<details>
   <summary>Collapse</summary>

      Data Science Salaries Dataset Exploration

        + Imports
        + Data
        + Basic EDA
            1. Missing Values
            2. Quantative Data
            3. Qualitative Data
        + Feature Engineering
            1. Adding coordinates for countries
            2. Adding new column with country names
            3. Adding new column with user experience
            4. Adding new column with employment type
            5. Replacing remote ratio numbers with names
            6. Replacing values in the company size
            7. Saving the final dataset
        + Example of a User Choice in the App
        + Salary ranges per chosen domain
            1. Example histogram with all domains with salary values in seaborn
        + Average salaries per chosen experience type
        + Experience level and Type of Employment
        + Highest salaries per domain per employment type
        + Choroplet world map showing the average salaries per country
        + Company size and average salary
        + Top 5 job postings in a chosen domain
</details> 


## Acknowledgments
<a name="Acknowledgments"></a>
Thank you to my mentor Akarsha Sehwag, as she was integral in introducing me to the world of data science app deployment.


## Licences
<a name="Licences"></a>

[Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)

## Contact
<a name="Contact"></a>

Find me on [LinkedIn](https://www.linkedin.com/in/tanja-ad%C5%BEi%C4%87/), [Twitter](https://twitter.com/adzic_tanja) or [adzictanja.com](https://www.adzictanja.com/).