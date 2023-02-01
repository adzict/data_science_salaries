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
    st.markdown("<h1 style='text-align: center; color: black;'>Salary trends in the Data Science field</h1>", unsafe_allow_html=True)
    
    #short description of the project
    st.markdown('Before embarking on the journey of a job search, it is important to know current trends in the industry, as well as a salary range to be able to negotiate during your job hunt. This application will give you detailed insights of salary trends in the Data Science domain in the last 2 years. You can customize your search per specific job position, country, remote or on-site work, as well as your experience.')

    #banner image
    image = Image.open('assets/handshake_banner_1.jpg')
    st.image(image, caption='Handshake Black and White')


#USER INPUT --------------------

with user_input:
    #header
    st.markdown("<h2 style='text-align: center; color: blue;'>Please choose options that best suit your profile:</h2>", unsafe_allow_html = True)

    #user input on specific domain
    domain_list = salaries['domain'].unique().tolist()
    user_domain = st.selectbox('Choose your domain:', domain_list)
    st.write('You selected:', user_domain)

    st.markdown("""---""")

    #user input on their experience level
    xp_list = salaries['experience_level'].unique().tolist()
    user_experience = st.selectbox('Choose your level of experience: ', xp_list)
    st.write('You selected:', user_experience)

    st.markdown("""---""")

    #user input on the employment type
    empl_type_list = salaries['employment_type'].unique().tolist()
    user_employment_type = st.selectbox('Choose the type of employment: ', empl_type_list)
    st.write('You selected:', user_employment_type)

    st.markdown("""---""")

    #user input on the employment location
    user_employment_loc = st.selectbox('What is your preference regarding the employment location: ', options = ['Remote', 'Hybrid', 'On-Site'])
    st.write('You selected:', user_employment_loc)

    st.markdown("""---""")

    #user input on the desired country
    country_list = salaries['company_country'].unique().tolist()
    user_target_country = st.selectbox('Select the desired location of the company: ', country_list)
    st.write('You selected:', user_target_country)



#OUTPUT --------------------------

#creating a dataframe with the user's preffered domain
user_domain_df = salaries.loc[salaries['domain'] == user_domain]

with output:
    #header
    st.markdown("<h2 style='text-align: center; color: green;'>Here is the overview of salaries based on the options you chose:</h2>", unsafe_allow_html = True)


    #OUTPUT AVG SALARIES ALL DOMAINS

    #plotting the seaborn distribution plot
    fig = sns.displot(salaries, x = 'salary_in_usd', hue = 'domain', kind = 'kde', multiple = 'stack', fill = True, aspect = 1, height = 8)
    plt.xlim(-100000, 600000)
    plt.ylabel('Sample Count', fontsize = 20)
    plt.xlabel('Salary in $', fontsize = 20)
    plt.title('Salary distribution across all domains', y = 1.1, loc='left', fontsize = 25)
    st.pyplot(fig)

    # OUTPUT AVG SALARIES ACROSS SELECTED DOMAIN AND ALL EXPERIENCES KDE PLOT

    #plotting the distribution kde plot
    fig = sns.displot(user_domain_df, x = 'salary_in_usd', hue = 'experience_level', kind = 'kde', multiple = 'stack', fill = True, aspect = 1, height = 8, palette = 'Set1')
    plt.xlim(-100000, 600000)
    plt.ylabel('Sample Count', fontsize = 20)
    plt.xlabel('Salary in $', fontsize = 20)
    plt.title(f'Salary distribution in the {user_domain} domain', y = 1.1, loc='left', fontsize = 25) 
    st.pyplot(fig)

    #OUTPUT WORLD MAP TARGET COUNTRY OF EMPLOYMENT AVG SALARY

    def create_map(user_target_country):

        # Filter the dataframe to only include the selected domain and country
        user_domain_country = salaries.loc[(salaries['domain'] == user_domain) & (salaries['company_country'] == user_target_country)]

        # Compute the average salary for the selected domain and country
        avg_salary_country = user_domain_country['salary_in_usd'].mean()

        # Create the map
        st.subheader(f'Average salary for the {user_domain} domain in {user_target_country} is ${avg_salary_country:.2f}')
        st.map(user_domain_country, zoom = 3)

    create_map(user_target_country)

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
