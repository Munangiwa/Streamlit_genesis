"""

    Author: Munangiwa Martin Hlongwane.

    Note:
    -----------------------------------------------------------------------------
    You need to PIP Install Streamlit first in your Anaconda prompt or terminal.
    -----------------------------------------------------------------------------

    Description: This file is used to launch  streamlit web
	application.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
##  Loading Libraries & Dependencies

# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
from PIL import Image

import numpy as np        # Fundamental package for linear algebra and multidimensional arrays
import pandas as pd       # Data analysis and manipulation tool

import requests
import io

# Importing modules for data science and visualization
import time
import timeit
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Quality of all figures in notebook
mpl.rcParams['figure.dpi'] = 180

# Load your raw data
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTP6Lbyw2u_hVCnwkPyzPIS90jJFGrmzMG8oZFR4Sji0TLMrYMOOfdkBxaCaDST6Fk-Hkqn6WQV0Njr/pubhtml?gid=0&single=true'
New_url = url.replace('pubhtml?gid=0&single=true', 'pub?output=csv')
raw = pd.read_csv(New_url)


# The main function where we will build the actual app
def main():
	"""Some Descriptive statistics for the given Data"""


	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Home","Analysis"]
	selection = st.sidebar.selectbox("Choose Option", options)

	# Building out the "Home" page
	if selection == "Home":
		st.title("Descriptive Statistic")
		image = Image.open('Descriptive.jpg')
		st.image(image)
		st.header("Introduction")
		st.info("This APP is designed to to give Descriptive Statistics of given data.")

	# Building out the EDA page
	if selection == "Analysis":
		st.subheader("Raw Data")
		
		if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
			st.session_state['number_of_rows'] = 5 
			st.session_state['type'] = 'Numerical'

		increament = st.button('Show more columns👆')
		if increament:
			st.session_state.number_of_rows = 20


		decrement = st.button('Show fewer columns👇')
		if decrement:
			st.session_state.number_of_rows = 2
		st.table(raw.head(st.session_state['number_of_rows']))

		def handle_click(new_type):
				st.session_state.type = new_type

		def handle_click_wo():
			if st.session_state.kind_of_column:
				st.session_state.type = st.session_state.kind_of_column



		type_of_column = st.radio("Which Feaure to Analyse",['Feature1','Feature2','Feature3','Feature4'], on_change = handle_click_wo,key = 'kind_of_column')
		#change == st.button('Change', on_click=handle_click,args = [type_of_column])
		if st.session_state['type'] =='Feature1':
			#Distribution =  pd.DataFrame(raw['Feature1'])
			st.info("Table below show the descriptive statics for Feature1")
			raw1 = raw['Feature_1'].describe(include='all')
			st.table(raw1)
			st.info('Feature_1 boxplot')
			fig = plt.figure(figsize=(15,8))
			sns.boxplot(x=raw['Feature_1'], data=raw)
			st.pyplot(fig)

		if st.session_state['type'] =='Feature2':
			
			st.info("Table below show the descriptive statics for Feature2")
			raw2 = raw['Feature_2'].describe(include='all')
			st.table(raw2)
			st.info('Feature_2 boxplot')
			fig = plt.figure(figsize=(15,8))
			sns.boxplot(x=raw['Feature_2'], data=raw)
			st.pyplot(fig)


		if st.session_state['type'] =='Feature3':
		
			st.info("Table below show the descriptive statics for Feature3")
			raw3 = raw['Feature_3'].describe(include='all')
			st.table(raw3)
			st.info('Feature_3 boxplot')
			fig = plt.figure(figsize=(15,8))
			sns.boxplot(x=raw['Feature_3'], data=raw)
			st.pyplot(fig)

		if st.session_state['type'] =='Feature4':
			
			st.info("Table below show the descriptive statics for Feature4")
			raw4 = raw['Fueature_4'].describe(include='all')
			st.table(raw4)
			st.info('Feature_4 boxplot')
			fig = plt.figure(figsize=(15,8))
			sns.boxplot(x=raw['Fueature_4'], data=raw)
			st.pyplot(fig)

	#if selection == "Comparison":
			#fig = plt.figure(figsize=(15,8))
			#sns.boxplot(y=raw['Feature_1','Feature_2','Feature_3','Fueature_4'], data=raw)
			#st.pyplot(fig)



# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
