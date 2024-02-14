import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightpink;padding:16px">
    <h2 style= "color:black";text-align:center> Health Insurance Cost Prediction App
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model= joblib.load('LinearRegression.pkl')
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
        
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
        
      
if __name__ == '__main__' :
    main()
