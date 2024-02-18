Overview:-

Smart phones have become a most useful tool in our daily life for communication with advanced technology provided intelligent assistance to the user in their everyday activities. The portable working framework with computing ability and interconnectivity, application programming interfaces for executing outsiders’ tools and applications, mobile phones have highlights such as cameras, GPS, web browsers so on., and implanted sensors such as accelerometers and gyroscope which permits the improvement of applications in view of client’s specific area, movement and context.

Activity Recognition (AR) is monitoring the liveliness of a person by using smart phone. Smart phones are used in a wider manner and it becomes one of the ways to identify the human’s environmental changes by using the sensors in smart mobiles. Smart phones are equipped in detecting sensors like gyroscope and accelerometer. The contraption is demonstrated to examine the state of an individual.

Human Activity Recognition (HAR) framework collects the raw data from sensors and observes the human movement using different deep learning approach. Deep learning models are proposed to identify motions of humans with plausible high accuracy by using sensed data.

HAR Dataset from UCI dataset storehouse is utilized. This dataset is collected from 30 persons (referred as subjects in this dataset), performing different activities with a smartphone to their waists. The data is recorded with the help of sensors (accelerometer and Gyroscope) in that smartphone. This experiment was video recorded to label the data manually.

This project is to build a model that predicts the human activities such as Walking, Walking_Upstairs, Walking_Downstairs, Sitting, Standing and Laying.

Datasetlink:-https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones

Project Details:-

In this project, we first we perform data preparation then eda which is stored in one file i.e. ActivityRecognotion.ipynb file.
then apply ml models like logistic regression, decision tree, linear svm, rbf svm & random forest for model training, prediction, evaluation, hyperparameter tuning and crossvalidation.
After applying all models compare each model with accuracy and error. All this activities stored in ActivityRecognitionUsingML.ipynb file.
Then make a streamlit app for recognizing activity in which user can upload test file then after clicking on predict they will find maximum activity human perform as well as countplot of all activity.

Applink:-https://activityrecognition.streamlit.app/

Test file and model used in this app is also uploaded for testing. App file is activity.py file.
