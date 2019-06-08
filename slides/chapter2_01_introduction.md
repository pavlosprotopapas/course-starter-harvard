---
type: slides
---

# Introduction

Notes: In the first chapter, I will give you the necessary intuitions to help you become familiar with the basics of linear regression.

- __[Linear regression](https://en.wikipedia.org/wiki/Linear_regression)__ it is used to approximate the dependency relationship between a dependent variable Y, the independent variables X<sub>i</sub> and a random term ε. 

This model can be expressed as:

![regression lineal model](./regression_lineal_model.jpg)
where :

+ Y<sub>t</sub> it is the dependent variable.
+ X<sub>1</sub>, X<sub>2</sub>, ... , X<sub>p</sub> are the explanatory variables.
+ &beta;<sub>0</sub>, &beta;<sub>1</sub>, &beta;<sub>2</sub>, ... ,&beta;<sub>p</sub>, are the parameters, measure the influence that the explanatory variables.
    
---

# Lest create a basic amount of data for this example and visualise it in a plot:

```python
import numpy as np
import matplotlib.pyplot as plt

number_points = 100
beta0 = 1
beta1 = 2

x = np.linspace(0, 1, num=number_points)
y = beta0 + beta1*x + np.random.normal(loc=1, scale=0.2, size=number_points)

plt.plot(x, y, '*') 
```

<div style="text-align:center">
    <img src="./visual_representation.png" 
    alt="Visual representation of the data generates in this example" 
    width="40%">
</div>

Notes: In this plot we can see ...

---

# Fit a linear regression model over the data generated :

<div style="text-align:center">
    <img src="./visual_representation_fit.png" 
    alt="Visual representation of the data generates in this example" 
    width="70%">
</div>

Notes: The following objective it fit a linear model over the data that generate before.

---

# Let's practice!
