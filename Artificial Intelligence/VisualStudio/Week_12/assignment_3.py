# -*- coding: utf-8 -*-
"""Assignment_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
"""

!pip install tensorflow scikeras scikit-learn

import pandas as pd
import numpy as np
import keras
import tensorflow as tf
from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from scikeras.wrappers import KerasClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, roc_auc_score, accuracy_score
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import RMSprop
from sklearn.preprocessing import LabelEncoder

from google.colab import drive
drive.mount('/content/drive')

"""#Extracting relevant features from the dataset"""

data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/CustomerChurn_dataset.csv')

data.head()

data.info()

data.replace(' ', np.nan, inplace=True)

data.isnull().sum()

# Specify the column to impute missing values
column_to_impute = 'TotalCharges'

imputer = SimpleImputer(strategy='mean')

data[[column_to_impute]] = imputer.fit_transform(data[[column_to_impute]])

data.drop('customerID', axis=1, inplace=True)

# Initialize LabelEncoder
label_encoder = LabelEncoder()
data['Churn'] = label_encoder.fit_transform(data['Churn'])

# Split the data into features and target
X = data.drop('Churn', axis=1)
y = data['Churn']

categorical_columns = data.select_dtypes(include=['object']).columns

# Display the categorical columns
print("Categorical Columns:")
print(categorical_columns)

# Extract numerical columns
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns

# Display the numerical columns
print("Numerical Columns:")
print(numerical_columns)

# Define categorical and numerical columns
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService',
       'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'Contract', 'PaperlessBilling', 'PaymentMethod']
numerical_cols = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']





















X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

# Get feature importances
feature_importances = rf_model.feature_importances_

# Create a DataFrame to display feature importances
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})

# Sort the DataFrame by importance in descending order
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Display the feature importances
print(feature_importance_df)

# Plot the feature importances
plt.bar(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Random Forest Feature Importance')
plt.xticks(rotation='vertical')
plt.show()

threshold = 0.02  # Adjust the threshold as needed
important_features = X.columns[feature_importances > threshold]
X_selected = X[important_features]
X_selected

X=X_selected

# Standardize the data
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)














"""#Exploratory Data Analysis"""

# X_selected.shape

# # Summary statistics
# print(X_selected.describe())

# # Pie chart for a single categorical variable
# # plt.figure(figsize=(8, 8))
# # data['Churn'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue'])
# # plt.title('Pie Chart for Churn')
# # plt.show()

# """From this pie chart, less customers churn"""

# #Boxplot for the numerical variables
# numericals = ['TotalCharges', 'MonthlyCharges', 'tenure','Contract']

# fig, ax = plt.subplots(1, 3, figsize=(15,8))
# for variable, subplot in zip(numericals, ax.flatten()):
#   sns.boxplot(x=data['Churn'], y=new_df[variable], ax=subplot, palette='Set2').set_title(str(variable))

# Categorical = ['Month-to-month', 'Two year', 'One year']

# sns.countplot(x=data['Contract'], hue=data['Churn'], palette = "Set2")

# """Customers who pay month to month can easily churn, however, those who paid for one year or two year contracts are less likely to churn. Hence, the people who pay month-to-month will churn a lot.

# # """

# Categorical = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)']

# sns.countplot(x=data['PaymentMethod'], hue=data['Churn'], palette = "Set2")

# """Customers who pay through Electric check are more likely to churn than those that pay with other methods.















# #Multi-Layer Perceptron model using the Functional API


# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # Keras Functional API model
# def create_model(optimizer='adam',hidden_layer1_units=64,hidden_layer2_units=32):
#   input_layer = Input(shape=(X_train.shape[1],))
#   hidden_layer_1 = Dense(hidden_layer1_units, activation='relu')(input_layer)
#   hidden_layer_2 = Dense(hidden_layer2_units, activation='relu')(hidden_layer_1)
#   output_layer = Dense(1, activation='sigmoid')(hidden_layer_2)

#   model = Model(inputs=input_layer, outputs=output_layer)
# #   model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
# #   return model

#   # Wrap the Keras model using KerasClassifier
# model = KerasClassifier(model=create_model, epochs=10, batch_size=32, verbose=0, hidden_layer1_units=32, hidden_layer2_units=16)

# # Define a parameter grid for grid search
# param_grid = {
#     'optimizer':['adam','sgd','rmsprop'],
#     'hidden_layer1_units':[32,64,128],
#     'hidden_layer2_units':[16,32,64]
# }






















# auc_scorer=make_scorer(roc_auc_score, greater_is_better=True)
# # Use GridSearchCV to find the best parameters
# grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring=auc_scorer, cv=StratifiedKFold(n_splits=5), verbose=1, error_score='raise')

# # Suppress TensorFlow warnings
# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, module="tensorflow")

# grid_result = grid_search.fit(X_train, y_train)

# print(f'Best Parameters: {grid_result.best_params_}')
# print(f'Best AUC Score: {grid_result.best_score_}')

# #Evaluate the best model on the test set
# best_model=grid_result.best_estimator_
# y_pred=best_model.predict(X_test)
# y_pred_binary=(y_pred>0.5).astype(int)
# accuracy_best=accuracy_score(y_test,y_pred_binary)
# auc_score_best=roc_auc_score(y_test,y_pred)
# print(f'Test Accuracy (Best Model): {accuracy_best}')
# print(f'AUC Score (Best Model): {auc_score_best}')



















"""#Model Optimization"""

#Define the model using optimized hyperparameters

input_layer = Input(shape=(X_train.shape[1],))
hidden_layer_1 = Dense(128, activation='relu')(input_layer)
hidden_layer_2 = Dense(32, activation='relu')(hidden_layer_1)
output_layer = Dense(1, activation='sigmoid')(hidden_layer_2)

optimized_model = Model(inputs=input_layer, outputs=output_layer)
optimized_model.compile(optimizer=RMSprop(learning_rate=0.001, rho=0.9), loss='binary_crossentropy', metrics=['accuracy'])


optimized_model.fit(X_train,y_train,epochs=10,batch_size=32,verbose=1)

y_optimized_pred=best_model.predict(X_test)
y_pred_optimized_binary=(y_pred>0.5).astype(int)

accuracy_optimized=accuracy_score(y_test,y_pred_optimized_binary)
auc_score_optimized=roc_auc_score(y_test,y_optimized_pred)

print(f'Test Accuracy (Optimized Model): {accuracy_optimized}')
print(f'AUC Score (Optimized Model): {auc_score_optimized}')

























import pickle

#Define the file path where you want to save the model
model = optimized_model

with open('model.pkl', 'wb') as file:
  pickle.dump(model, file)

with open('scaler.pkl', 'wb') as scaler_file:
  pickle.dump(scaler, scaler_file)

with open('model.pkl', 'rb') as file:
  loaded_model=pickle.load(file)

with open('scaler.pkl', 'rb') as scaler_file:
  loaded_scaler=pickle.load(scaler_file)