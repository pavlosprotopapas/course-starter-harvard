---
type: slides
---

# Introduction


![regression lineal model](./regression_lineal_model.jpg)
where :

+ Y<sub>t</sub> it is the dependent variable.
+ X<sub>1</sub>, X<sub>2</sub>, ... , X<sub>p</sub> are the explanatory variables.
+ &beta;<sub>0</sub>, &beta;<sub>1</sub>, &beta;<sub>2</sub>, ... ,&beta;<sub>p</sub>, are the parameters, measure the influence that the explanatory variables.
    
---

# Keras Basics (Defining a model):

```python
from keras.models import Sequential
from keras.layers import Dense,Activation
model=Sequential() #This is used to define that this model is a sequential model

model.add() #This function is used to add layers to the model

```
We'll be using two types of layers for now: <br>
A 'Dense' layer, which is a fully connected layer <br>
An 'Activation' layer, which just applies an activation function to the input
```python
model.add(Dense(p1,input_dim=p2)) 
#input_dim specifies the number of nodes in the input layer, in this case p2 input nodes
#p1 specifies the number of nodes in the first hidden layer

model.add(Dense(p1))
#This specifies a layer with p1 nodes

model.add(Activation('relu')
#This defines an activation function
```
---

# Training the model

```python
model.compile(loss='mean_squared_error',optimizer='adam') #Compiles the model

model.fit(X,Y,epochs=z) #Trains the NN model
#X in the input variable
#Y is the target variable
#z is the number of epochs to train for  
```
---

# Let's practice!
