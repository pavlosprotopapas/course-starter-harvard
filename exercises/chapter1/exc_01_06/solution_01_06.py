import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

data_filename = 'https://raw.githubusercontent.com/pavlosprotopapas/course-starter-harvard/master/jn/data.csv'
df = pd.read_csv(data_filename)

# Set beta0 = 2.2
beta0 = 2.2

# Create lists to store the MSE and beta1
MSE = []
beta1_list = []

for beta1 in np.arange(0, 3, 0.1):
    y_predict = beta0 + beta1 * df.x

    # Append the new MSE in the list that you created above
    MSE.append(np.mean((df.y - y_predict) ** 2))

    # Also append beta1 values in the list
    beta1_list.append(beta1)

# Plot MSE as a function of beta1
plt.plot(beta1_list, MSE)
