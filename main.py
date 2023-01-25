#IMPORTS
import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#CONTAINERS FOR STREAMLIT
header = st.container()
user_input = st.container()
output = st.container()
footer = st.container()

#DATASET 
#checking if the dataset loads
st.subheader('dataset check')

salaries = pd.read_csv('data/ds_salaries_domain.csv', index_col=0, sep=';')
st.write(salaries.head())

#HEADER

with header:
    #title of the project
    st.title('Salary trends in the Data Science field')

    #short description of the project
    st.markdown('Before embarking on the journey of a job search, it is important to know current trends in the industry, as well as a salary range to be able to negotiate during your job hunt. This application will give you detailed insights of salary trends in the Data Science domain in the last 2 years. You can customize your search per specific job position, country, remote or on-site work, as well as your experience.')

    #banner image
    image = Image.open('assets/handshake_banner_1.jpg')
    st.image(image, caption='Handshake Black and White')


#USER INPUT

with user_input:
    st.header('Please choose below options that best suit your profile:')

    #creating Select and Display columns
    sel_col, display_col = st.columns(2)

    #user input on specific domain
    user_domain = sel_col.selectbox('Choose your domain: ', options = ['Data Science', 'Data Engineering', 'Data Analysis', 'Machine Learning Engineering', 'Research'])

    #user input on their experience level
    user_experience = sel_col.selectbox('Choose your level of experience: ', options = ['Entry level / Junior', 'Intermediate level', 'Senior / Expert level', 'Executive / Director level'])

    #user input on the employment type
    user_employment_type = sel_col.selectbox('Choose the type of employment: ', options = ['Full Time', 'Part Time', 'Contract', 'Freelance'])

    #user input on the employment location
    user_employment_loc = sel_col.selectbox('What is your preference regarding the employment location: ', options = ['Remote', 'Hybrid', 'On-Site'])

    #user input on the desired country
    user_target_country = sel_col.selectbox('Select the country where you wish to work: ', options = ['remote', 'country'])



#OUTPUT

with output:
    st.subheader('Here is the OUTPUT')

    st.markdown('* Salaries for >domain< range from X to Y in >country<')
    st.markdown('* Bar chart showing salaries per employment type')
    st.markdown('* Bar chart showing salaries per location of the employment')
    st.markdown('* World map showing neighbouring countries and AVG salary for >domain< ')
    st.markdown('* Some job postings under >domain< domain include: >list of top 10 unique positions<')

#FOOTER

with footer:
    st.subheader('Dataset Source:')
    st.subheader('Contact Me: ')
