import streamlit as st
from nltk.corpus import stopwords
import string
import joblib

clf = joblib.load('svm.plk')
tfidf = joblib.load('tfidf.plk')

stopwords = set(stopwords.words('english'))

def remove_punc(txt) :
    txt = txt.lower()
    return txt.translate(str.maketrans('','',string.punctuation))

def remove_num(txt):
    new = ''
    for i in txt :
        if not i.isdigit():
            new = new + i
    return new

def remove_emoji(txt):
    new = ''
    for i in txt :
        if i.isascii():
            new = new + i
    return new

st.title('Fake News Predictor')
title = st.text_input('Enter title')
text = st.text_input('Enter text')
data = str(title) + str(text)

final_data = tfidf.transform([data])
btn = st.button('Find')


if btn :
    st.balloons()
    pred = clf.predict(final_data)
    if pred == 1:
        st.success("This is not a fake news")
    
    else :
        st.success("This is  a fake news")



