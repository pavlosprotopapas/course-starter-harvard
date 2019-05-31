import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# Set beta0 = 2.2
beta0 = 2.2

# Create lists to store the MSE and beta1
MSE = ____;
beta1_list = ____;

for beta1 in np.arange(0, 3, 0.1):
    y_predict = beta0 + beta1 * df.x

    # Append the new MSE in the list that you created above
    MSE.____;

    # Also append beta1 values in the list
    beta1_list.____;

# Plot MSE as a function of beta1 
plt.plot(beta1_list, MSE)
