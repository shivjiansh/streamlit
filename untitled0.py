#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:10:06 2022

@author: shivansh
"""

import numpy as np
import pickle
import streamlit as st


loaded_mod = pickle.load(open('/home/shivansh/Downloads/trained_model.sav', 'rb'))


def db_predict(input_data):
   
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
    #std_data = scaler.transform(input_data_reshaped)
    #print(std_data)

    prediction = loaded_mod.predict(input_data_reshaped)
    #print(prediction)

    if (prediction[0] == 0):
      return 'safee'
    else:
      return 'in danger'
  
    
  
    
def main():
    #giving a title
    st.title('Safe Hearts')
    
    #	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal

    age = st.text_input('age')
    Sex = st.text_input('Gender')
    cp = st.text_input('Chest Pain')
    trestbps = st.text_input("Resting BP")
    chol = st.text_input('Cholestrol Level')
    fbs = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting ECG')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
  
   
   
    diagno = ''
   
    if st.button('Predict'):
       diagno = db_predict([age, Sex, cp, trestbps, chol, fbs,	restecg,	thalach,	exang,	oldpeak,	slope,	ca,	thal])
       
     
        
    st.success(diagno)
    
    
if __name__ == '__main__':
    main()
