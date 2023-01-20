<h1 align="center">
             MedicalHelp 🩺 💊 💉
</h1>
  
## Overview of the App

This app is used to predict the current medical state of an individual regarding 3 most common diseases and also includes a section which will provide some medical guidelines to anyone who is affected by any common disease from the disease prediction section.

The disease sections include ->

**1. Covid-19 Prediction Section**

**2. Diabetes Prediction Section**

**3. Heart Disease Prediction Section**

## Tech Stacks Used

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

## Libraries Used

<img src="https://img.shields.io/badge/numpy%20-%2314354C.svg?&style=for-the-badge&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas%20-%2314354C.svg?&style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/pickle%20-%2314354C.svg?&style=for-the-badge&logo=pickle&logoColor=white"/>
<img src="https://img.shields.io/badge/flask%20-%2314354C.svg?&style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/scikitlearn%20-%2314354C.svg?&style=for-the-badge&logo=scikitlearn&logoColor=white"/> <img src="https://img.shields.io/badge/html5%20-%2314354C.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css3%20-%2314354C.svg?&style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/bootstrap%20-%2314354C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>

## Structure Of The Project

- The home page consists of cards which contains the links to 4 different web pages in which 3 are medical prediction section and 1 is medical guideline section.
- The prediction sections include - Diabetes Prediction, Covid-19 Prediction, Heart Disease Prediction.
- Each prediction page is conneceted with a Machine Learning Model which uses Random Forest Classifier to predict whether the user is affected by that disease or not.
- Also we have 3 different datasets used for training each of the machine learning model. The models are then stored in a pickle file and connected with the web pages using Flask.
- Each of the 3 web pages associated with prediction contains forms which take 4 different feature as input from the user in a given specified range in number format.
- The value entered in the forms are then fed into each of the individual models for getting the prediction. According to the predicted values the user is alerted whether they are a victim to that disease or not.
- The most relevant features are taken into consideration for prediction also these features can be found out with simple tests or analysis without visiting any doctor.
- So the victim can get a broad overview of their health condition specially regarding 3 most common diseases without any kind of doctor appointments.

## The features taken into consideration

| Disease | Features |
| - | - |
| Covid-19 | Dry Cough, Fever, Sore Throat, Breathing Problem |
| Diabetes | Glucose, Insulin, Body Mass Index, Age |
| Heart Disease | Chest Pain, Blood Pressure, Cholestrol, Max Heart Rate |

The feature selection is carefully done under the supervision of a medical science student.

## Model Deployment

- The web application is built using python library -> Flask and Web Programming languages -> HTML, CSS, Bootstrap
- The entire application is finally deployed on Heroku by adding - Procfile (informs Heroku that which application is to be run first), Requirements (notifies Heroku about the libraries that needs to be installed before deploying or running our application)

## Future Prospects

- Addition of more disease prediction sections to cover more segments of medical domain
- Inclusion of a NLP chatbot for users to get advice regarding their diet and nutrition chart 
- Addition of a quiz section which will take inputs about the common diseases covered in the application and mark them as wrong and right to give users a detailed info regarding their disease

#### RUN LOCALLY:

1. pip install -r requirements.txt

2. python3 app.py

#### RUN TESTS:

****Keep the server running and run below command**** 

pytest -q test.py