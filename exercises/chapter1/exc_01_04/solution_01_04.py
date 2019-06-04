import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.read_csv(data_filename)

# Rename columns in data frame as [x,y]
df.columns = ['x', 'y']

# Plot axis x vs axis y
plt.plot(df.x, df.y, 'bs')
