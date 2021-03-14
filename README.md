# project

Objective of the project: To predict whether a patient will end up in ICU or not 

datacleaning.py is used for data cleaning. It involves imputing missing values and performing one-hot encoding.The goal here is to clean and make sure utilize most of the data in model building.

modelbuilding.py is used for buliding models that can predict whether the patient will end up in ICU.

There are a few things to note. There a lot of NAN values in the dataset which will hinder the model buliding process. Therefore the best way would be to impute the missing values with previous values. A separate file is included(missing values.py). However this process leads to having NAN values in earlier time windows. This will lead to data loss and hinder the performance of the model. Therefore, the missing values have been imputed with mean values. 

A combination of models have been used and their performance has been evaluated.

First, records with the earlier time window(0-2) are taken separately to test and compare the model's performance with other time windows


Model Building:

Logistic Regression:
Since this is a binary classification problem, I have chosen a few models based to predict based on their 
Gaussian Naive Bayes:

Boosting:

SVM_Linear:

SVM_radial: 

# Deploying models using Flask
model.py - This contains code for our Machine Learning model to predict whether the person ends up in ICU or not
app.py - This contains Flask APIs that receives details through API calls and computes the precited value based on our model and returns it.
request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
templates - This folder contains the HTML template to allow user to enter pateint detail and displays the predicted result.

Run using command:
python model.py
This will a file model2.pkl

Run using command to acess Flask API
python app.py

Navigate to URL http://localhost:5000

Enter valid values in all input boxes and hit Predict

![prediction](https://user-images.githubusercontent.com/51070088/111088767-2f4c7980-84ff-11eb-95b1-e54d481b54c5.JPG)
