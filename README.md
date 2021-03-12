# project

Objective of the project: To predict whether a patient will end up in ICU or not 

datacleaning.py is used for data cleaning. It involves imputing missing values and performing one-hot encoding.The goal here is to clean and make sure utilize most of the data in model building.

modelbuilding.py is used for buliding models that can predict whether the patient will end up in ICU.

There are a few things to note. There a lot of NAN values in the dataset which will hinder the model buliding process. therefore the best way would be to impute the missing values with previous values. A separate file is included(missing values.py). However this process leads to having NAN values in earlier time windows. This will lead to data loss and hinder the performance of the model. Therefore, the missing values have been imputed with mean values. 

A combination of models have been used and their performance has been evaluated.

First, records with the earlier time window(0-2) are taken separately to test and compare the model's performance with other time windows
