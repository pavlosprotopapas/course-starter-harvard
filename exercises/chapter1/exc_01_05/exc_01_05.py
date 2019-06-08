# import numpy and name it np
import numpy as np

# import matplotlib.pyplot
import matplotlib.pyplot as plt

import pandas as pd

# add the following line in order to have the plots inside the notebook
%matplotlib inline

# read the data
data_filename = 'https://raw.githubusercontent.com/Harvard-IACS/2018-CS109A/master/content/lectures/lecture5/data/Advertising.csv'
df = pd.read_csv(data_filename);

#  columns in data frame as [x,y]
df = df.iloc[5:13]


# Select the columns I need to simplify the rest of the code
data_x = df.TV
data_y = df.sales


# Here's a function that finds the index of the nearest neighbor
# and returns the value of the nearest neighbor.  Note that this
# is just for k = 1 and the distance function is simply the
# absolute value.
def find_nearest(df, value):
    data_x = df.TV

    idx = (np.abs(data_x - value)).idxmin()
    return idx, data_x[idx]


# Note that we have used the idxmin method in our function.  This is
# because `array' is a pandas dataframe and idxmin() is designed to
# work with pandas dataframes.  If we are working with a numpy array
# then the appropriate method would be `argmin()'.

# Create some artificial x-values (might not be in the actual dataset)
x =__

# Initialize the y-values to zero
y = np.zeros((len(x)))

# Apply the KNN algorithm.  Try to predict the y-value at a given x-value
# Note:  You may have tried to use the `range' method in your code.  Enumerate
# is far better in this case.  Try to understand why.
for i, xi in enumerate(x):
    y[i] =___

# Plot your solution
plt.plot(x, y, '-')
# Plot the original data using black x's.
plt.plot(df.TV, df.sales, 'k+')
plt.title('')
plt.xlabel('TV budget in $1000')
plt.ylabel('Sales in $1000')
