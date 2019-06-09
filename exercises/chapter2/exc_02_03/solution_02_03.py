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

# Set beta0 = 2.2
beta0 = 6.67

# Create lists to store the MSE and beta1
MSE = []
beta1_list = []

for beta1 in np.arange(-1, 2, 0.01):
    y_predict = beta0 + beta1 * df_new.TV

    # Append the new MSE in the list that you created above
    MSE.append(np.mean((df_new.sales - y_predict) ** 2))

    # Also append beta1 values in the list
    beta1_list.append(beta1)

# Plot MSE as a function of beta1
plt.plot(beta1_list, MSE)
plt.xlabel('Beta1')
plt.ylabel('MSE')

# To display all figures
plt.show()