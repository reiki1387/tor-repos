# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn import tree

warnings.filterwarnings('ignore')

# Creating a synthetic dataset
# This dataset simulates customer data for a telecom company
data = {
      'CustomerID': range(1, 101),  # Unique ID for each customer
      'Age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]*10,  # Age of customers
      'MonthlyCharge': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]*10,  # Monthly bill amount
      'CustomerServiceCalls': [1, 2, 3, 4, 0, 1, 2, 3, 4, 0]*10,  # Number of customer service calls
      'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']*10  # Churn status
}
df = pd.DataFrame(data)


# Splitting the dataset into features and target variable
# Features include age, monthly charge, and customer service calls
# The target variable is churn (Yes or No)
X = df[['Age', 'MonthlyCharge', 'CustomerServiceCalls']]
y = df['Churn']

# Splitting the dataset into training and testing sets
# 70% of the data is used for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training the Decision Tree model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Making predictions on the test set
y_pred = clf.predict(X_test)

# Evaluating the model using accuracy
# Accuracy is the proportion of correct predictions among the total number of cases processed
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')


#ACCURACY TABLE VISUALIZATION
import pandas as pd

# Create a comparison table
results = pd.DataFrame({
    'Actual': y_test,          # True answers
    'Predicted': y_pred,       # Model's guesses
    'Correct?': y_test == y_pred  # Checks if matching
})

print("\nTest Paper Visualization:")
print(results.head(10))  # Show first 10 questions

# Calculate accuracy manually to demonstrate
correct = sum(y_test == y_pred)
total = len(y_test)
manual_accuracy = correct / total

print(f"\nManual Accuracy Check: {correct} correct / {total} total = {manual_accuracy:.2f}")



# PLOT FOR ACCURACY-CONFUSION MATRIX HEATMAP
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Predicted No', 'Predicted Yes'],
            yticklabels=['Actual No', 'Actual Yes'])
plt.title('Churn Prediction Accuracy')
plt.show()




# PLOT TREE Improved visualization
# plt.figure(figsize=(20, 12))

# # Customize the plot with better styling
# plot_tree(clf, 
#           filled=True, 
#           rounded=True,  # Rounded boxes
#           feature_names=['Age', 'MonthlyCharge', 'CustomerServiceCalls'], 
#           class_names=['No Churn', 'Churn'],
#           fontsize=8,  # Larger font
#           node_ids=True,  # Show node numbers
#           #proportion=True,  # Show proportions instead of counts -values
#           impurity=True)  # Hide/Show Gini to reduce clutter

# # Add title and adjust layout
# plt.title("Customer Churn Decision Tree (Improved Visualization)", 
#           fontsize=14, pad=8)
# plt.show()




# #TRUE VS PREDICTED PLOT
# df_results = pd.DataFrame({'True': y_test, 'Predicted': y_pred})
# df_results = df_results.reset_index(drop=True)

# plt.figure(figsize=(10, 4))
# plt.plot(df_results['True'], label='True', marker='o')
# plt.plot(df_results['Predicted'], label='Predicted', marker='x')
# plt.legend()
# plt.title('True vs Predicted Churn')
# plt.xlabel('Sample')
# plt.ylabel('Churn')
# plt.show()


# #SCATTER PLOT
# # Map churn labels to numeric for scatter plot
# label_map = {'No': 0, 'Yes': 1}
# y_test_numeric = y_test.map(label_map).reset_index(drop=True)
# y_pred_numeric = pd.Series(y_pred).map(label_map)

# plt.figure(figsize=(10, 6))
# plt.scatter(range(len(y_test_numeric)), y_test_numeric, label='True', marker='o', color='blue')
# plt.scatter(range(len(y_pred_numeric)), y_pred_numeric, label='Predicted', marker='x', color='orange')
# plt.yticks([0, 1], ['No', 'Yes'])
# plt.title('Scatter Plot: True vs Predicted Churn')
# plt.xlabel('Sample Index')
# plt.ylabel('Churn')
# plt.legend()
# plt.grid(True)
# plt.show()





# #FEATURE IMPORTANT PLOT 
# import numpy as np

# # Get feature importances
# importances = clf.feature_importances_
# features = ['Age', 'MonthlyCharge', 'CustomerServiceCalls']
# print(dict(zip(features, clf.feature_importances_)))

# # Sort features by importance
# indices = np.argsort(importances)[::-1]

# # Create plot
# plt.figure(figsize=(10,6))
# plt.title("Feature Importance in Customer Churn Prediction", fontsize=14)
# plt.bar(range(len(importances)), importances[indices], color='skyblue', align='center')
# plt.xticks(range(len(importances)), [features[i] for i in indices], fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlabel("Features", fontsize=12)
# plt.ylabel("Relative Importance", fontsize=12)

# # Add values on top of bars
# for i, v in enumerate(importances[indices]):
#     plt.text(i, v+0.01, f"{v:.2f}", ha='center', fontsize=12)

# plt.tight_layout()
# plt.show()



#Confusion Matrix
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# cm = confusion_matrix(y_test, y_pred, labels=['No', 'Yes'])
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Churn', 'Churn'])
# disp.plot(cmap='Blues')
# plt.title('Confusion Matrix')
# plt.show()






# #Decision Boundary Plot (for 2 features)
# from sklearn import tree
# import numpy as np

# # Use only two features
# X2 = X[['Age', 'MonthlyCharge']]
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.3, random_state=42)

# clf2 = DecisionTreeClassifier()
# clf2.fit(X2_train, y2_train)

# # Create meshgrid
# x_min, x_max = X2['Age'].min() - 5, X2['Age'].max() + 5
# y_min, y_max = X2['MonthlyCharge'].min() - 5, X2['MonthlyCharge'].max() + 5
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 1),
#                      np.arange(y_min, y_max, 1))

# Z = clf2.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = pd.Series(Z).map({'No': 0, 'Yes': 1}).values.reshape(xx.shape)

# plt.figure(figsize=(8, 6))
# plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
# plt.scatter(X2_test['Age'], X2_test['MonthlyCharge'], c=y2_test.map({'No': 0, 'Yes': 1}), cmap='coolwarm', edgecolor='k')
# plt.xlabel('Age')
# plt.ylabel('MonthlyCharge')
# plt.title('Decision Boundary of Decision Tree (2 features)')
# plt.show()


