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

# Set beta0 = 2.2
beta0 = 2.2

# Create lists to store the MSE and beta1
MSE = ____;
beta1_list = ____;

for beta1 in np.arange(0, 3, 0.1):
    y_predict = beta0 + beta1 * df.?

    # Append the new MSE in the list that you created above
    MSE.____;

    # Also append beta1 values in the list
    beta1_list.____;

# Plot MSE as a function of beta1
plt.plot(beta1_list, MSE)
