# Project

Objective of the project: To predict whether a patient will end up in ICU or not.

Data cleaning involves imputing missing values and performing one-hot encoding.The goal here is to clean and make sure utilize most of the data in model building.

Classfication models are used that can predict whether the patient will end up in ICU.

# There are a few things to note.
There a lot of NAN values in the dataset which will hinder the model buliding process. Therefore the best way would be to impute the missing values with previous values. However this process leads to having NAN values in earlier time windows. This will lead to data loss and hinder the performance of the model. Therefore, the missing values have been imputed with mean values. 

A combination of models have been used and their performance has been evaluated.

First, records with the earlier time window(0-2) are taken separately to test and compare the model's performance with other time windows. 

The models have been only applied to the earliest window(0-2) due to time constraint and must be further applied to other windows.


Model Building:
Models used in this project are:

Logistic Regression
Gaussian Naive Bayes
Boosting
SVM_Linear
SVM_radial 

The performance and other issues such as multicollinearity have been discussed in the Project_submission.ipynb file. A variety of libraries has been imported for exploration purposes, please ignore them.


# Deploying models using Flask
model.py - This contains code for our Machine Learning model to predict whether the person ends up in ICU or not.

app.py - This contains Flask APIs that receives details through API calls and computes the precited value based on our model and returns it.

request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.

templates - This folder contains the HTML template to allow user to enter pateint detail and displays the predicted result.

Run using command:
python model2.py
This will give a file model1.pkl

Run using command to acess Flask API
python app.py

URL to access flask http://localhost:5000

Enter valid values in all input boxes and hit Predict

![prediction2](https://user-images.githubusercontent.com/51070088/111093536-940fd000-850f-11eb-9311-f613dda8e726.JPG)

![prediction](https://user-images.githubusercontent.com/51070088/111088767-2f4c7980-84ff-11eb-95b1-e54d481b54c5.JPG)


#PLEASE NOTE: There is a file project_submission.py and a file model2.py. The difference in the files are the features and the number of models. Deployment has been done using logistic regression and a limited number of features.


Futher more, this flask app can been hosted using AWS EC2 instance with the following steps:
1. Connect to EC2 instance 
2. In the app.py change the last line of the script to app.run(host='0.0.0.0', port=8080)
3. Upload the files app.py, model2.py, templates and requests.py to ec2 instance using winscp
4. Install python using the command yum install python3
5. Run it using python3 app.py

This will ensure that we do not need a local machine to access flask.



