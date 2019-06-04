# Import the numpy library and name it np
import numpy as np
# Import the pandas library and name it pd
import pandas as pd


# Read data.csv file using pandas libraries
data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.read_csv(data_filename);

# Check number of observations and number of columns, mean values of x and y etc
df.describe()
