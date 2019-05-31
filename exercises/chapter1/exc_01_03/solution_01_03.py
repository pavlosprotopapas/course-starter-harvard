# Import the pandas library and name it pd 
import pandas as pd

# Read data.csv file using pandas libraries 
df = pd.read_csv('data.csv')

# Check number of observations and number of columns, mean values of x and y etc 
df.describe()
