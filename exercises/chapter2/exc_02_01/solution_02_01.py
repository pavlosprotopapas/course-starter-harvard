# import matplotlib.pyplot
import matplotlib.pyplot as plt

import pandas as pd

# add the following line in order to have the plots inside the notebook
%matplotlib inline

# read the data
data_filename = 'https://raw.githubusercontent.com/Harvard-IACS/2018-CS109A/master/content/lectures/lecture5/data/Advertising.csv'
df = pd.read_csv(data_filename);

#  rename columns in data frame as [x,y]
df.columns = ____;

# Plot  x vs  y
plt.____;