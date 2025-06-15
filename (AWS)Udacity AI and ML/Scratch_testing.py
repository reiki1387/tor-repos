# Import necessary libraries
import pandas as pd  # For handling and analyzing data in table format (DataFrames)
import numpy as np  # For numerical operations and creating arrays
import matplotlib.pyplot as plt  # For creating plots and charts
import seaborn as sns  # A higher-level interface for data visualization based on matplotlib
import warnings  # To manage warning messages

# Scikit-learn modules for machine learning tasks
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.ensemble import RandomForestRegressor  # A machine learning model for regression tasks
from sklearn.metrics import mean_squared_error  # To evaluate model accuracy using MSE



data_size = 500

# Create a synthetic (fake but realistic) dataset
# Each "feature" here represents some building characteristics
# data_size means to create 500 random values for each building feature.
data = {
    'WallArea': np.random.randint(200, 400, data_size),  # Random integers for wall area
    'RoofArea': np.random.randint(100, 200, data_size),  # Random integers for roof area
    'OverallHeight': np.random.uniform(3, 10, data_size),  # Random floats for building height
    'GlazingArea': np.random.uniform(0, 1, data_size),  # Random floats for window-to-wall ratio
    'EnergyEfficiency': np.random.uniform(10, 50, data_size)  # Target variable: energy efficiency score
}

# Convert the data dictionary into a DataFrame for easier handling
df = pd.DataFrame(data)
# print("This is df:\n", df)



X = df.drop('EnergyEfficiency', axis=1)  # Drop the target column to get the input features
y = df['EnergyEfficiency']  # This is what we want to predict
# print("This is Y:\n", y)
# print("This is X:\n", X)

# sns.pairplot(df, 
#              x_vars=['WallArea', 'RoofArea', 'OverallHeight', 'GlazingArea'], 
#              y_vars='EnergyEfficiency', 
#              height=6, aspect=0.5, kind='scatter')
# plt.show()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# print ("This is X-train\n", X_train)
# print ("This is X-test\n", X_test)
# print ("This is y-train\n", y_train)
# print ("This is y-test\n", y_test)

model = RandomForestRegressor()

# Train the model on the training data
model.fit(X_train, y_train)

# ----------- Model Prediction and Evaluation -----------

# Use the trained model to make predictions on the test data
predictions = model.predict(X_test)
# print (predictions)

# Evaluate how good the predictions are using Mean Squared Error (lower is better)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

#Plot 1: Actual vs predicted value
# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, predictions)  # Each point represents one prediction
# plt.xlabel("True Values- Actual Energey Efficiency")  # What the actual energy efficiency was
# plt.ylabel("Predictions")  # What the model predicted
# plt.title("True Values vs Predicted Values")
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')  # Diagonal line for perfect prediction
# plt.show()


#Plot 2: Prediction Errors (Residual Plot)
errors = y_test - predictions

plt.figure(figsize=(8, 6))
plt.scatter(predictions, errors, alpha=0.7, color='tomato')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel("Predicted Energy Efficiency")
plt.ylabel("Prediction Error (Actual - Predicted)")
plt.title("Prediction Error Plot")
plt.grid(True)
plt.show()


# VISUALIZING A SINGLE TREE
# from sklearn.tree import plot_tree

# # Get feature names from your DataFrame
# feature_names = X.columns  # or X_train.columns
# # Visualize the first tree in the forest
# plt.figure(figsize=(20, 10))
# plot_tree(model.estimators_[0], 
#           feature_names=feature_names,
#           filled=True, 
#           rounded=True, 
#           max_depth=3)  # limit to 3 levels
# plt.show()


# WHAT FEATURES MODEL RELY ON
# importances = model.feature_importances_
# feature_names = X_train.columns

# # Plot it
# plt.figure(figsize=(8, 5))
# plt.barh(feature_names, importances)
# plt.xlabel("Importance")
# plt.title("Feature Importance in Random Forest")
# plt.show()