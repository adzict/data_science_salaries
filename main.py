#IMPORTS
import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
from plotly.figure_factory import create_distplot

#PAGE LAYOUT
st.set_page_config(page_title = 'Data Science Salaries', page_icon = 'random', layout= "centered", initial_sidebar_state="auto", menu_items = {'Get Help': 'mailto: adzic.tanja@gmail.com', 'About': 'www.adzictanja.com'})

#CONTAINERS FOR STREAMLIT ----
header = st.container()
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
    st.markdown("<h1 style='text-align: center;'>Salary trends in the Data Science field</h1>", unsafe_allow_html=True)
    
    #short description of the project
    st.markdown('Before embarking on the journey of a job search, it is important to know current trends in the industry, as well as a salary range to be able to negotiate during your job hunt. This application will give you detailed insights of salary trends in the Data Science domain in the last 2 years. It is designed to help you understand how different factors, such as location, experience level, and employment type, impact salaries in the field.')

    #banner image
    image = Image.open('assets/handshake_banner_1.jpg')
    st.image(image, caption='Handshake Black and White')


#USER INPUT --------------------

with st.sidebar:
    #header
    st.markdown("<h2 style='text-align: center; color: red;'>Please choose options that best suit your profile:</h2>", unsafe_allow_html = True)

    #user input on specific domain
    domain_list = salaries['domain'].unique().tolist()
    user_domain = st.selectbox('Choose your domain:', domain_list)

    #user input on their experience level
    xp_list = salaries['experience_level'].unique().tolist()
    user_experience = st.selectbox('Choose your level of experience: ', xp_list)
    
    #user input on the employment type
    empl_type_list = salaries['employment_type'].unique().tolist()
    user_employment_type = st.selectbox('Choose the type of employment: ', empl_type_list)

    #user input on the employment location
    user_employment_loc = st.selectbox('What is your preference regarding the employment location: ', options = ['Remote', 'Hybrid', 'On-Site'])

    #user input on the desired country
    country_list = salaries['company_country'].unique().tolist()
    user_target_country = st.selectbox('Select the desired location of the company: ', country_list)

#OUTPUT --------------------------

#creating a dataframe with the user's preffered domain
user_domain_df = salaries.loc[salaries['domain'] == user_domain]

with output:
    #header
    st.markdown("<h2 style='text-align: center; color: gray;'>Here is the overview of salaries based on the options you chose:</h2>", unsafe_allow_html = True)


    #OUTPUT AVG SALARIES ALL DOMAINS

    #plotting the seaborn distribution plot
    fig = sns.displot(salaries, x = 'salary_in_usd', hue = 'domain', kind = 'kde', multiple = 'stack', fill = True, aspect = 1, height = 8)
    plt.xlim(-100000, 600000)
    plt.ylabel('Sample Count', fontsize = 20)
    plt.xlabel('Salary in $', fontsize = 20)
    plt.title('Salary distribution across all domains', y = 1.1, loc='left', fontsize = 25)
    st.pyplot(fig)

    #LINE BREAK
    st.markdown('---')

    # OUTPUT AVG SALARIES ACROSS SELECTED DOMAIN AND ALL EXPERIENCES KDE PLOT

    #plotting the distribution kde plot
    fig = sns.displot(user_domain_df, x = 'salary_in_usd', hue = 'experience_level', kind = 'kde', multiple = 'stack', fill = True, aspect = 1, height = 8, palette = 'Set1')
    plt.xlim(-100000, 600000)
    plt.ylabel('Sample Count', fontsize = 20)
    plt.xlabel('Salary in $', fontsize = 20)
    plt.title(f'Salary distribution in the {user_domain} domain', y = 1.1, loc='left', fontsize = 25) 
    st.pyplot(fig)

    #LINE BREAK
    st.markdown('---')

    #OUTPUT WORLD MAP TARGET COUNTRY OF EMPLOYMENT AVG SALARY

    #world map of avg salaries per country
    avg_salary_world = salaries.groupby(['alpha-3', 'company_country']).agg({'salary_in_usd' : ['mean']}).stack().reset_index()
    avg_salary_world.head()

    fig = px.choropleth(avg_salary_world, locations = 'alpha-3',
                   color = 'salary_in_usd', hover_name = 'company_country', title = "Average Salaries per Country",
                   color_continuous_scale='viridis',
                   height = 500)
    st.plotly_chart(fig)

    #specific country with the average for that domain
    def create_map(user_target_country):

        # Filter the dataframe to only include the selected domain and country
        user_domain_country = salaries.loc[(salaries['domain'] == user_domain) & (salaries['company_country'] == user_target_country)]

        # Compute the average salary for the selected domain and country
        avg_salary_country = user_domain_country['salary_in_usd'].mean()

        # Create the map
        st.subheader(f'Average salary for the {user_domain} domain in {user_target_country} is ${avg_salary_country:.2f}')
        st.map(user_domain_country, zoom = 3)

    create_map(user_target_country)

    #LINE BREAK
    st.markdown('---')

    #OUTPUT AVG SALARIES PER EMPLOYMENT TYPE

    st.subheader(f'Average salaries for {user_domain} domain if you wish to work {user_employment_type} are:')

    #creating the dataframe with chosen employment type and experience level
    user_xp_empl = salaries[(salaries['experience_level'] == user_experience) & (salaries['employment_type'] == user_employment_type)]

    #plotting the barchart
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(user_xp_empl, x = 'remote_ratio', y = 'salary_in_usd', palette = 'Set2', errorbar = None)
    plt.bar_label(ax.containers[0])
    plt.ylabel('Salary in $', fontsize = 12)
    plt.xlabel('Employment Location', fontsize = 12)
    plt.title(f'Average Salaries per Employment Location for the {user_experience}', fontsize = 15)
    st.pyplot(fig)

    #LINE BREAK
    st.markdown('---')

    #OUTPUT AVERAGE SALARIES PER DOMAIN PER EMPLOYMENT TYPE

    st.subheader(f'Average salaries per domain and per employment type:')

    #plotting the barchart
    fig = plt.figure(figsize=(12,6))
    sns.barplot(salaries, x = 'salary_in_usd', y = 'domain', hue = 'remote_ratio', palette = 'rainbow', errorbar = None)
    plt.ylabel('', fontsize = 16)
    plt.xlabel('Salary in $', fontsize = 16)
    plt.title(f'Average Salaries for all domains with respect to Employment Type', fontsize = 19)
    st.pyplot(fig)

    #LINE BREAK
    st.markdown('---')

    #OUTPUT AVG SALARY IN RESPECT TO COMPANY SIZE PER CHOSEN DOMAIN
    
    #filtering out data needed for the pie chart: labels and avg salary
    company_size = user_domain_df.groupby('company_size').agg({'salary_in_usd' : ['mean']}).stack().reset_index()

    #pie_chart
    #defining the data for the pie chart
    labels = company_size['company_size']
    sizes = company_size['salary_in_usd']
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    #plotting the pie chart
    plt.pie(sizes, labels=labels, colors=colors, explode=(0.1, 0.1, 0.1), autopct='%1.1f%%')
    plt.title(f'Average Salaries per Company Size for the {user_domain} domain', fontsize = 15)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    #LINE BREAK
    st.markdown('---')

    #OUTPUT TOP 5 JOB NAMES UNDER THAT DOMAIN

    st.subheader(f'Top 5 Job Postings examples in the {user_domain} domain are:')

    #getting the list of the top 5 job postings
    dict_jobs = user_domain_df['job_title'].value_counts()[:5].to_dict()
    list_jobs = list(dict_jobs.keys())

    #displaying the list in a markdown
    for i in list_jobs:
        st.markdown("- " + i)

#FOOTER

with footer:

    #LINE BREAK
    st.markdown('---')


    st.subheader('Dataset Source:')
    st.markdown('This dataset was aggregated from the ai-jobs.net Salaries, and can be obtained from the Kaggle website: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries')

    #LINE BREAK
    st.markdown('---')


    st.subheader('Contact Me: ')

    st.markdown('www.adzictanja.com')
    st.markdown('www.github.com/adzict')
    st.markdown('www.linkedin.com/in/tanja-ad??i??')
