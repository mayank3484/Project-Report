import streamlit as st
import joblib
from PIL import Image
import plotly.express as px
import pandas as pd
from pathlib import Path
st.text(Path.cwd())
def title():
    html_temp = """
        <div style="background-color:lightpink;padding:16px">
        <h2 style= "color:black";text-align:center> Health Insurance Cost Prediction App
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

def main():
       
        
        
        
    model= joblib.load('Streamlit/LinearRegression')
    p1= st.number_input('Enter Your Age in range 18 to 100',18,100,"min",1,format="%d")
    s1= st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
    
    p3= st.number_input("Enter your BMI Value in range 15 to 54 ",15.000,54.000,"min",0.001,format="%.1f")
    
    p4=st.slider('Enter the No. of Children',0,5)
    s2=st.selectbox('Smoker',('yes','no'))
    
    if s2=='yes':
        p5=1
    else:
        p5=0
    s3=st.selectbox('Region',('SouthWest','SouthEast','NorthWest','NorthEast'))
    if s3=='SouthWest':
        p6=3
    elif s3=='SouthEast':
        p6=2
    elif s3=='NorthWest':
        p6=1
    else:
        p6=0
    
    
    
    if st.button('Predict'):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        if pred>0:
            st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
            st.header("what cause such a high health insurance cost?")
            tab1, tab2, tab3 = st.tabs(["Smoking","BMI","Age"])
            transformed_data=pd.read_csv('Streamlit/transformed.csv')
            with tab1:
                fig1=px.histogram(data_frame=transformed_data,x="smoker",y="charges",opacity=0.6,histfunc='avg')
                st.plotly_chart(fig1)
                st.markdown(
                    "Smoking cause a very drastic impact on the health and impacts cost of insurance. So if you "
                    "want to reduce cost of insurance then you have to quit smoking.")
            with tab2:
                fig2=px.scatter(data_frame=transformed_data,x="bmi",y="charges",opacity=0.6)
                st.plotly_chart(fig2)
                st.write("As your body mass index or bmi increases insurance cost increases. So it is better to "
                        "reduce weight that reduce your bmi and insurance cost.")
            with tab3:
                fig3 = px.scatter(data_frame=transformed_data,x='age',y='charges',opacity=0.6)
                st.plotly_chart(fig3)
                st.write("At older ages, Insurance cost is more and increased with age")
        else:
            pred=0
            st.success('Your Insurance Cost is {} .You do not need insurance '.format(pred))

        

            
def main_page():
    title()
    main()        
      
if __name__ == '__main__' :
    main_page()
