# import matplotlib.pyplot
import matplotlib.pyplot as plt

import pandas as pd

# add the following line in order to have the plots inside the notebook
%matplotlib inline

# read the data
data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.read_csv(data_filename)

# Rename columns in data frame as [x,y]
df.columns = ____;

# Plot  x vs  y
plt.____;
