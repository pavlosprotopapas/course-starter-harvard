# import matplotlib.pyplot
import matplotlib.pyplot as plt

import pandas as pd

# add the following line in order to have the plots inside the notebook
%matplotlib inline

# read the data
data_filename = 'https://raw.githubusercontent.com/Harvard-IACS/2018-CS109A/master/content/lectures/lecture5/data/Advertising.csv'
df = pd.read_csv(data_filename);

#  Select 7 rows
df = df.iloc[0:7]

# Plot Sales vs TV
plt.plot(df.TV, df.sales, 'b+')

# Add axis labels for clarity
plt.xlabel('TV budget')
plt.ylabel('Sales')