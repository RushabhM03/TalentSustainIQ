# TalentSustainIQ🧠
### An optimized employee retention algorithm

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is an xgboost powered algorithm that takes several factors regrading the employment history of an employee and the outputs whether or not the employee is likely to stay at the company

## 🎱 Problem statement
Nowadays, employees are switching organizations at a rapid pace. The task is to build a machine learning model that can take various hr inputs and output whether or not the employee is likely to stay or not.TAking care of the needs of each and every employee is a challenging task for the HR department. This may result in talents leaving the company. 

## 〽️ Phases 

- Data exporation and visualization
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

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.


## 🎯 Project setup

Clone the project

```
git clone 
```

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

