import numpy as np
import pandas as pd

npoints = 30
beta0 = 2.2
beta1 = 1.2
epsillon = 0.75

x = np.linspace(0, 4, num=npoints)
y = beta0 + beta1 * x + np.random.normal(loc=0, scale=epsillon, size=npoints)

mydf = pd.DataFrame({'x': x, 'y': y})

mydf.to_csv('data.csv', index=False)

# Import the pandas library and name it pd

# Read data.csv file using pandas libraries
df = pd.____;

# Check number of observations and number of columns, mean values of x and y etc
df.____;
