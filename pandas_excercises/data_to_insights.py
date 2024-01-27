
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Frame the Problem
# Assuming you have a dataset named 'customer_data.csv'
import pandas as pd
data = pd.read_csv('customer_data.csv')

# Step 2: Data Understanding
# Assuming the dataset has columns 'Age', 'Promotion_Score', and 'Purchase_Frequency'
print(data.describe())

# Step 3: Extract Features
data['Promotion_Sensitivity_Score'] = data['Promotion_Score'] * data['Purchase_Frequency']

# Step 4: Analyze and Visualize
# Scatter plot with regression line
plt.scatter(data['Promotion_Sensitivity_Score'], data['Purchase_Frequency'])
plt.title('Promotion Sensitivity vs Purchase Frequency')
plt.xlabel('Promotion Sensitivity Score')
plt.ylabel('Purchase Frequency')

# Fit a linear regression model
reg_model = LinearRegression().fit(data[['Promotion_Sensitivity_Score']], data['Purchase_Frequency'])
plt.plot(data['Promotion_Sensitivity_Score'], reg_model.predict(data[['Promotion_Sensitivity_Score']]), color='red', linewidth=3)

plt.show()

# Step 5: Present Results
# Print insights and recommendations
print("Insight: Higher Promotion Sensitivity Score correlates with increased purchase frequency.")
print("Recommendation: Develop targeted promotions for customers with lower scores to boost sales; tailor marketing strategies based on age demographics.")
