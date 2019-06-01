import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

df = pd.read_csv('data.csv')

# Estimate beta0 by observing the value of y when x = 0
beta0 = ____;

# Estimate beta1! Check the slope for guidance
beta1 = ____;

# Define the function to calculate the prediction of x using beta0 and beta1
y_predict = ____;

# Plot the predicted values as well as the data
plt.plot(df.x, df.y, 'bs')
plt.plot(df.x, y_predict)

# Calculate the MSE
MSE = ____;

# Print the results
print("My MSE is: {0}".format(MSE))
