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

#  Select 7 rows
df = df.___

# Plot TV vs Sales
plt.___

# Add axis labels for clarity (x : TV budget, y : Sales)
plt.___
plt.___

# To display all figures
plt.show()
