import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
% matplotlib
inline

df = pd.read_csv('data.csv')

# Estimate beta0 by observing the value of y when x = 0
beta0 = 1.5

# Estimate beta1! Check the slope for guidance
beta1 = 1.5

# Define the function to calculate the prediction of x using beta0 and beta1
y_predict = beta0 + beta1 * df.x

# Plot the predicted values as well as the data
plt.plot(df.x, df.y, 'bs')
plt.plot(df.x, df)

# Calculate the MSE
MSE = np.mean((df.y - y_predict) ** 2)  # MSE = ...

# Print the results
print("My MSE is: {0}".format(MSE))
