#Import pandas to read in the data
import pandas as pd
#Import Keras to build to neural network
from keras.models import Sequential
from keras.layers import Dense,Activation
import matplotlib.pyplot as plt
#Reading in the data. y is the label we are trying to predict
df=pd.read_csv('https://raw.githubusercontent.com/amanmalali/Stride/master/two_humps.csv')
X=df['x']
Y=df['y']

#Define the model architecture here as follows:
#input layer with one node -> hidden layer with four nodes -> output layer with one nodes

print('Model Summary')
model.summary() #Prints the model layers summary

model.compile(loss='mean_squared_error',optimizer='adam') 
model.fit(X,Y,epochs=___) #Train the model for any number of epochs

predictions=model.predict(X) #Predict values for x

plt.scatter(___) #Plot the original x vs y plot
plt.scatter(___) #Plot the x vs predictions plot
plt.show()
