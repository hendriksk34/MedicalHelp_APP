import pytest
import requests
import pickle
import numpy as np

model1 = pickle.load(open('diabetesmodel.pkl', 'rb'))
model2 = pickle.load(open('covid19model.pkl', 'rb'))
model3 = pickle.load(open('heartdiseasemodel.pkl', 'rb'))

def test_diabetespredict():
    json = {"glucose": 100,"insulin": 300,"body mass index":50,"age":30}
    response_login = requests.post("http://127.0.0.1:5000/diabetes", json)
    assert response_login.status_code == 200

def test_covid19predict():
    json = {"Dry Cough": 10,"Fever": 10,"Sore Throat":8,"Breathing Problem":20}
    response_login = requests.post("http://127.0.0.1:5000/covid", json)
    assert response_login.status_code == 200

def test_heartdiseasepredict():
    json = {"Chest Pain": 1,"Blood Pressure": 80,"Cholestrol":150,"Max Heart Rate":120}
    response_login = requests.post("http://127.0.0.1:5000/heartdisease", json)
    assert response_login.status_code == 200

def test_havingheartdiseasemodel():
    values = [4,200,500,120]
    int_features = [int(x) for x in values]
    final_features = [np.array(int_features)]
    prediction = model3.predict(final_features)
    assert prediction == "Presence"

def test_nothavingheartdiseasemodel():
    recent_values = [1,80,125,100]
    int_features = [int(x) for x in recent_values]
    final_features = [np.array(int_features)]
    prediction_check = model3.predict(final_features)
    assert prediction_check == "Absence"

def test_havingcovidmodel():
    values = [200,200,200,200]
    int_features = [int(x) for x in values]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)
    assert prediction == 1

def test_nothavingcovidmodel():
    values = [10,10,10,10]
    int_features = [int(x) for x in values]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)
    assert prediction == 0

def test_havingdiabestesmodel():
    values = [200,500,60,30]
    int_features = [int(x) for x in values]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)
    assert prediction == "Yes"

def test_nothavingdiabestesmodel():
    values = [0,0,0,10]
    int_features = [int(x) for x in values]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)
    assert prediction == "No"