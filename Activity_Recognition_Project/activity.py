import streamlit as st
import pandas as pd
import joblib
from sklearn.svm import LinearSVC
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt

def title():
    html_temp = """
        <div style="background-color:lightpink;padding:16px">
        <h2 style= "color:black";text-align:center> Activity Recognition App
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

def main():
       
    s1=st.selectbox('Format of the file',('Text','CSV'))
    
    if s1=='Text':
        test_file=st.file_uploader('Upload text file contain Inertial data and feature',type={'txt'})
        if test_file is not None:
            test_data=pd.read_csv(test_file, delim_whitespace=True, header=None)
            model=joblib.load('Activity_Recognition_Project/LinearSVM.pkl')
            if st.button('Predict'):
                pred=model.predict(test_data)
                st.success('Maximum Activity that human performing is {}'.format(prediction_df.value_counts().head(1)))
                
                plt.figure(figsize=(16,8))
                
                plt.title('Data provided by each user', fontsize=20)
                fig1=px.histogram( prediction_df)
                fig1.update_layout(
                    title='Countplot of Activities',
                    xaxis_title='ActivityName',
                    yaxis_title='Counts',
                    template='plotly_white'
                )
                st.plotly_chart(fig1)
    else:
        input_data=st.file_uploader("Upload Smartphone inertial data in csv file",type={"csv"})
        if input_data is not None:
            test_df=pd.read_csv(input_data)
            test_df=test_df.drop(['subject','Activity','ActivityName'],axis=1)
                        
            model=joblib.load('Activity_Recognition_Project/LinearSVM.pkl')
            if st.button('Predict'):
                pred=model.predict(test_df)
                prediction_df=pd.DataFrame(pred)
                st.success('Maximum Activity that human performing is {}'.format(prediction_df.value_counts().head(1)))
                plt.figure(figsize=(16,8))
                
                plt.title('Data provided by each user', fontsize=20)
                fig1=px.histogram( prediction_df)
                fig1.update_layout(
                    title='Countplot of Activities',
                    xaxis_title='ActivityName',
                    yaxis_title='Counts',
                    template='plotly_white'
                )
                st.plotly_chart(fig1)

            
def main_page():
    title()
    main()        
      
if __name__ == '__main__' :
    main_page()
