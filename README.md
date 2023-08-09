# TalentSustainIQ🧠
### An optimized employee retention algorithm

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is an xgboost-powered algorithm that takes several factors regarding the employment history of an employee and outputs whether or not the employee is likely to stay at the company

## 🎱 Problem statement
Nowadays, employees are switching organizations at a rapid pace. The task is to build a machine learning model that can take various hr inputs and output whether or not the employee is likely to stay or not. Taking care of the needs of each and every employee is a challenging task for the HR department. This may result in talents leaving the company. 

## 〽️ Phases 

- Data exploration and visualization
- Data preprocessing
- Model Selection
- Model building
- API making
- UI design

## 🚀 Features

- REST API to train the model using training batch dataset
- REST API to predict the result using the prediction batch dataset
- Proper UI with pages explaining the project and steps to follow
- Corporate news page
- API dashboard management system
- log keeping
- data management
- dynamic model selection
- database storage

## 💻 Techstack
- Flask
- Python
- HTML
- Tailwind css
- Tensorflow
- Sqlite

[![My Skills](https://skillicons.dev/icons?i=flask,python,html,tailwindcss,tensorflow,sqlite&perline=6)](https://skillicons.dev)


## 🉐 Model selections
Decision Trees:

>Imagine you have a dataset with different features (like age, income, etc.) and a target variable (like whether a person will buy a product or not).
A decision tree is like a flowchart that divides the data based on the features, trying to separate the target classes (e.g., "buy" or "not buy").
Each split in the tree is based on a specific feature and a threshold value for that feature.

Residuals:

>Residuals are the errors or mistakes made by the model in predicting the target variable.
For example, if the model predicts that someone will buy the product, but in reality, they don't, then the residual for that data point is the difference between the predicted value and the actual value.
XGBoost focuses on reducing these residuals.

Ensemble Learning:

>XGBoost uses multiple decision trees (called an ensemble) to make predictions.
Each tree in the ensemble tries to correct the mistakes of the previous trees.

Gradient Boosting:

>XGBoost uses a technique called "gradient boosting" to train the trees in the ensemble.
Gradient refers to the direction and magnitude of improvement needed to reduce the residuals.
In simple terms, XGBoost looks at the mistakes made by the current ensemble of trees and trains the next tree to do a better job at correcting those mistakes.

Learning Rate:

>The learning rate is a small number that controls how much each new tree contributes to the ensemble.
A low learning rate makes the algorithm learn slowly and more carefully, while a high learning rate makes it learn quickly and more aggressively.

Regularization:

>XGBoost has some techniques to prevent overfitting (when the model is too complex and memorizes the training data).
Regularization in XGBoost adds penalties for overly complex trees, making the model more generalizable.


In summary, XGBoost builds an ensemble of decision trees, where each tree learns to correct the mistakes of the previous trees using gradient information. The learning rate controls the step size for improvement, and regularization helps prevent overfitting. By combining the predictions of all the trees, XGBoost creates a powerful model that can make accurate predictions for classification or regression tasks.

Here d-trees and xgboost models are created from parameters like: 
> 'learning_rate': [0.5, 0.1, 0.01, 0.001],

> 'max_depth': [3, 5, 10, 20],

> 'n_estimators': [10, 50, 100, 200]

and the best model is selected from them


## 👩 Contributors
Team members

- [**R**ushabh Maru](https://github.com/RushabhM03) - rushabh.maru123@gmail.com


## 🎯 Project setup

Clone the project

```
git clone https://github.com/RushabhM03/TalentSustainIQ.git
```

Setup the Virtual environment
(Run the commands in the base folder)
```
virtualenv venv
cd venv/Scripts
& "Activate.psl"
cd.. cd ..
```

Environment variables
(Create a .env file)
```
NEWS_API_KEY="Your API key"
```

UI setup
(Run the URL on the browser)
```
http://localhost:5000/
```

Training
(Open Postman and run the API endpoint after having the correct data in the training_data folder)
```
http://0.0.0.0:5000/training
```

Testing/Batch prediction
(Open Postman and run the API endpoint after having the correct data in the prediction_data folder)
```
http://0.0.0.0:5000/batchprediction
```

NOTE: After training u can use the form UI on the website to make predictions


## API management

Below is a list of important APIs

| purpose | API |
| ------ | ------ |
| training | http://0.0.0.0:5000/training |
| batchprediction | http://0.0.0.0:5000/batchprediction |
| Single prediction | http://0.0.0.0:5000/prediction |
| API dashboard | https://localhost:5000/dashboard |

> username and password for dashboard = "admin"

