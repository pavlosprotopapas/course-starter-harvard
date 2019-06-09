# Import the numpy library and name it np
import numpy as np
# Import the pandas library and name it pd
import pandas as pd
# import matplotlib.pyplot
import matplotlib.pyplot as plt
# add the following line in order to have the plots inside the notebook
%matplotlib inline

# Data set used in this exercise (Advertising.csv)
data_filename = 'https://raw.githubusercontent.com/Harvard-IACS/' \
                '2018-CS109A/master/content/lectures/lecture5/data/Advertising.csv'

# Read Advertising.csv file using pandas libraries:
df = pd.read_csv(data_filename)

# Create a new dataframe called `df_new`. witch the columns ['TV' and 'sales'].
df_new = df[['TV', 'sales']]

# Estimate beta0 by observing the value of y when x = 0
beta0 = 6.67

# Estimate beta1! Check the slope for guidance
beta1 = 0.05

# Define the function to calculate the prediction of x using beta0 and beta1
y_predict = beta0 + beta1 * df_new.TV

# Plot the predicted values as well as the data
plt.plot(df_new.TV, df_new.sales, '*')
plt.plot(df_new.TV, y_predict)
plt.xlabel('TV')
plt.ylabel('Sales')

# To display all figures
plt.show()

# Calculate the MSE
MSE = np.mean((df_new.sales - y_predict) ** 2)

# Print the results
print("My MSE is: {0}".format(MSE))
