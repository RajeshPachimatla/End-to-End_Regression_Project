# End-to-End_Regression_Project
This project is about predicting the house rent in Hyderabad city, India based on the following features: Location, No of bedrooms, Sqft area of the flat, and whether it is furnished/semi-furnished/unfurnished. A LinearRegression model has been developed and deployed in a webpage of html/css/javascript which can do home pirce prection. 

DataFrame of the project as follows: 
1. Dataset of hyderabad rent prices has been taken from kaggle.com
2. Data science concepts such data cleaning, feature engineering, outlier removal, dimensional reduction, hot encoding and gridsearch CV has been performed and build the LinearRegression model
3. After the model is build, it was exported to a pickle file and used a python flask server which can consume this pickle file and do price prediction.
4. This python flask server will expose http ednpoints for various requests and ui returns in html/css/javascript 

Following the screen shot of the webpage which I run on the localserver
