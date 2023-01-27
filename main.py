#IMPORTS
import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#CONTAINERS FOR STREAMLIT ----
header = st.container()
user_input = st.container()
output = st.container()
footer = st.container()

#DATASET ----------------------

salaries = pd.read_csv('data/salaries_final.csv')

# #checking if the dataset loads
# st.subheader('dataset check')
# st.write(salaries.head())

#HEADER -----------------------

with header:
    #title of the project
    st.title('Salary trends in the Data Science field')

    #short description of the project
    st.markdown('Before embarking on the journey of a job search, it is important to know current trends in the industry, as well as a salary range to be able to negotiate during your job hunt. This application will give you detailed insights of salary trends in the Data Science domain in the last 2 years. You can customize your search per specific job position, country, remote or on-site work, as well as your experience.')

    #banner image
    image = Image.open('assets/handshake_banner_1.jpg')
    st.image(image, caption='Handshake Black and White')


#USER INPUT --------------------

with user_input:
    st.header('Please choose below options that best suit your profile:')

    #creating Select and Display columns
    sel_col, display_col = st.columns(2)

    #user input on specific domain
    domain_list = salaries['domain'].unique().tolist()
    user_domain = sel_col.selectbox('Choose your domain: ', domain_list, 0)

    #user input on their experience level
    xp_list = salaries['experience_level'].unique().tolist()
    user_experience = sel_col.selectbox('Choose your level of experience: ', xp_list, 0)

    #user input on the employment type
    empl_type_list = salaries['employment_type'].unique().tolist()
    user_employment_type = sel_col.selectbox('Choose the type of employment: ', empl_type_list, 0)

    #user input on the employment location
    user_employment_loc = sel_col.selectbox('What is your preference regarding the employment location: ', options = ['Remote', 'Hybrid', 'On-Site'])

    #user input on the desired country
    country_list = salaries['company_country'].unique().tolist()
    user_target_country = sel_col.selectbox('Select the desired location of the company: ', country_list, 0)



#OUTPUT --------------------------

with output:
    st.subheader('HERE GOES OUTPUT')

    #OUTPUT BAR CHART SALARIES IN DOMAIN (MEAN, MIN, MAX)

    if user_domain == 'Data Science':
        st.subheader('Average, minimum and maximum salaries for the Data Science domain are:')

        user_domain_df = salaries.loc[salaries['domain'] == user_domain]
        salary_ranges = user_domain_df.groupby('domain').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        #bar chart
        fig = plt.figure(figsize=(10, 4))
        ax = sns.barplot(salary_ranges, x = 'level_1', y = 'salary_in_usd')
        plt.bar_label(ax.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.yticks(rotation = 0)
        plt.title('Mean, minimum, and maximum values of salaries in the Data Science domain', fontsize = 12)
        st.pyplot(fig)

    elif user_domain == 'Data Engineering':
        st.subheader('Average, minimum and maximum salaries for the Data Engineering domain are:')

        user_domain_df = salaries.loc[salaries['domain'] == user_domain]
        salary_ranges = user_domain_df.groupby('domain').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        #bar chart
        fig = plt.figure(figsize=(10, 4))
        ax = sns.barplot(salary_ranges, x = 'level_1', y = 'salary_in_usd')
        plt.bar_label(ax.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.yticks(rotation = 0)
        plt.title('Mean, minimum, and maximum values of salaries in the Data Engineering domain', fontsize = 12)
        st.pyplot(fig)

    elif user_domain == 'Data Analysis':
        st.subheader('Average, minimum and maximum salaries for the Data Analysis domain are:')

        user_domain_df = salaries.loc[salaries['domain'] == user_domain]
        salary_ranges = user_domain_df.groupby('domain').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        #bar chart
        fig = plt.figure(figsize=(10, 4))
        ax = sns.barplot(salary_ranges, x = 'level_1', y = 'salary_in_usd')
        plt.bar_label(ax.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.yticks(rotation = 0)
        plt.title('Mean, minimum, and maximum values of salaries in the Data Analysis domain', fontsize = 12)
        st.pyplot(fig)

    elif user_domain == 'Machine Learning Engineering':
        st.subheader('Average, minimum and maximum salaries for the Machine Learning Engineering domain are:')

        user_domain_df = salaries.loc[salaries['domain'] == user_domain]
        salary_ranges = user_domain_df.groupby('domain').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        #bar chart
        fig = plt.figure(figsize=(10, 4))
        ax = sns.barplot(salary_ranges, x = 'level_1', y = 'salary_in_usd')
        plt.bar_label(ax.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.yticks(rotation = 0)
        plt.title('Mean, minimum, and maximum values of salaries in the Machine Learning Engineering domain', fontsize = 12)
        st.pyplot(fig)

    elif user_domain == 'Research':
        st.subheader('Average, minimum and maximum salaries for the Research domain are:')

        user_domain_df = salaries.loc[salaries['domain'] == user_domain]
        salary_ranges = user_domain_df.groupby('domain').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        #bar chart
        fig = plt.figure(figsize=(10, 4))
        ax1 = sns.barplot(salary_ranges, x = 'level_1', y = 'salary_in_usd')
        plt.bar_label(ax1.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.yticks(rotation = 0)
        plt.title('Mean, minimum, and maximum values of salaries in the Research domain', fontsize = 12)
        st.pyplot(fig)

    else:
        st.markdown('Something went wrong')

    
    #OUTPUT AVG SALARIES PER EXPERIENCE TYPE

    if user_experience == 'Intermediate Level':
        st.subheader('Average, minimum and maximum salaries for the Intermediate Level of exerience are:')

        user_xp_df = salaries.loc[salaries['experience_level'] == user_experience]
        salary_xp = user_domain_df.groupby('experience_level').agg({'salary_in_usd': ['mean', 'min', 'max']}).stack().reset_index()

        fig = plt.figure(figsize=(10, 4))
        ax2 = sns.barplot(salary_xp, x = 'level_1', y = 'salary_in_usd', cmap = 'Set2')
        plt.bar_label(ax2.containers[0])
        plt.ylabel('Salary in USD', fontsize=10)
        plt.yticks(rotation = 0)
        plt.xlabel('Ranges from Minimum, Maximum to Mean', fontsize=10)
        plt.title(f'Mean, minimum, and maximum values of salaries for the {user_experience}', fontsize = 12)
        st.pyplot(fig)

    #OUTPUT WORLD MAP TARGET COUNTRY OF EMPLOYMENT AVG SALARY

    st.subheader(f'Average salaries in {user_target_country} for {user_domain} domain are:')

    #OUTPUT AVG SALARIES PER EMPLOYMENT TYPE

    st.subheader(f'Average salaries for {user_domain} domain if you wish to work {user_employment_type} are:')

    #OUTPUT AVG SALARIES PER LOCATION OF THE EMPLOYMENT

    st.subheader(f'Average salaries for {user_domain} domain if your chosen location is {user_employment_loc} are:')

    #OUTPUT TOP 5 JOB NAMES UNDER THAT DOMAIN

    st.subheader(f'Top 5 Job Postings examples in the {user_domain} domain are:')


#FOOTER

with footer:
    st.subheader('Dataset Source:')
    st.subheader('Contact Me: ')
