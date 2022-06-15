import streamlit as st
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle
# st.write("Hello ,let's learn how to build a streamlit app together")

# st.title ("this is the app title")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')
age = st.slider('Age', 18,100)
jop = st.selectbox('Jop',['Employee','PrivateJob'])
if jop == 'Employee':
    jop = 0
else:
    jop = 1
Qualification = st.selectbox('Qualification',['HigherEdu','MiddleEdu','BasicEdu'])
if Qualification == 'HigherEdu':
    Qualification = 0
if Qualification == 'MiddleEdu':
    Qualification = 1
else:
    Qualification = 2

hstat = st.selectbox('Hstatus',['GoodHealth','Stable','ChronicDiseases'])
if hstat == 'GoodHealth':
    hstat = 0
if hstat == 'Stable':
    hstat = 1
else:
    hstat = 2
ManufacturingYear = int(st.date_input('ManufacturingYear').strftime('%Y'))


cc = st.slider('Cc', 600,4000)
vage = st.number_input('V Age', 0,50)

use = st.selectbox('Use',['Commercial','Private'])
if use == 'Commercial':
    use = 0
else:
    use = 1
vMileg = st.number_input('V Milege', 0,9999990)
premium = st.number_input('Premium', 0,9999990)
tclaim = st.selectbox('Tclaim',['High','Medium','Low'])
if tclaim == 'High':
    tclaim = 0
if tclaim == 'Medium':
    tclaim = 1
else:
    tclaim = 2
Insurance = st.number_input('InsuranceVal', 0,999999990)
# st.selectbox('Jop',['Employee','PrivateJob'])


if st.button('Calculate'):

    pickle_in = open("CarData.pickle", "rb")
    KNN = pickle.load(pickle_in)

    predicted= KNN.predict([[int(age),int(jop),int(Qualification),int(hstat),int(ManufacturingYear),int(cc),int(vage),int(use),int(vMileg),int(premium),int(tclaim),int(Insurance)]])
    
    if predicted == 1:
        st.error("rejection")
    else:
        st.success("acception")
    
    

    