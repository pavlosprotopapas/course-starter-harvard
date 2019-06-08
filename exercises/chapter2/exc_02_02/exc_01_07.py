# Import the numpy library and name it np
import numpy as np
# Import the pandas library and name it pd
import pandas as pd

# Read data.csv file using pandas libraries from
data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.____;

# Check number of observations and number of columns, mean values of x and y etc
df.____;


import pandas as pd
%matplotlib inline

data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.read_csv(data_filename)

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
