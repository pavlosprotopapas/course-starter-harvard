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

# Create a new dataframe called `df_new`. witch the columns [?,?]
df_new = df[['x', 'y']]

# Plot the data in a graphic of ? vs ?.
plt.plot(df_new.?, df_new.?, 'bs')

# To display all figures
plt.show()
