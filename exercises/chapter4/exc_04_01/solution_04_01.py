#Import pandas to read in the data
import pandas as pd
#Import Keras to build to neural network
from keras.models import Sequential
from keras.layers import Dense,Activation
import matplotlib.pyplot as plt
#Reading in the data. y is the label we are trying to predict
df=pd.read_csv('https://raw.githubusercontent.com/amanmalali/Stride/master/step.csv')
X=df['x']
Y=df['y']
model=Sequential() #Define the model to be sequential in nature
#Specifies the input layer has one node and the hidden layer has one node
model.add(Dense(1,input_dim=1))  #Performs a0=W0.x+b0

model.add(Activation('sigmoid')) #We use a sigmoid activation function here. z0=sigmoid(a0)

model.add(Dense(1)) #define the output layer with a linear activation z1=W1.z0+b1

print('Model Summary')
model.summary() #Prints the model layers summary

model.compile(loss='mean_squared_error',optimizer='adam') 
model.fit(X,Y,epochs=1000) #Train the model

predictions=model.predict(X) #Predict values for x

plt.scatter(df.x,df.y,label='original') #Plot the original x vs y plot
plt.scatter(df.x,predictions,label='prediction') #Plot the x vs predictions plot
plt.show()
