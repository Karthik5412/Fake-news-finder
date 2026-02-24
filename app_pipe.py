import streamlit as st
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
import string
import re

class preprocessing(BaseEstimator,TransformerMixin) :
    def fit(self,x,y=None) :
        return self
    
    def transform(self,x) :
        cleaned = []
        for text in x :
            text = re.sub(r'[^a-zA-z\s]','',text.lower())
            
            text.strip()
            
            cleaned.append(text)
            
        return cleaned
    
    
pipe = joblib.load('pipe_data.plk')

st.title('Fake News Predictor')
title = st.text_input('Enter title')
text = st.text_input('Enter text')
data = str(title) + str(text)

btn = st.button('Find')

if btn :
    st.balloons()
    if title == '' or text == '':
        st.success('Please enter text')
    else :
        pred = pipe.predict(data)
        if pred[0] == 1:
            st.success("This is not a fake news")
        
        else :
            st.success("This is  a fake news")