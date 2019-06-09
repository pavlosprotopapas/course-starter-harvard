---
title: 'Chapter 3: Introduction to Linear Regression'
description: 'Day 1 afternoon A.'
prev: /chapter2/
next: null
id: 2
type: chapter
---

<exercise id="6" title="Linear Regression Basics" type="slides">
    <slides source="chapter2_01_introduction"></slides>
</exercise>

<exercise id="7" title="Getting Started">

What does the estimated standard error of &beta;<sub></sub> represent?     

<choice>
<opt text="The standard deviation of the residuals ε.">This is not correct</opt>
<opt text="The uncertainty of the true slope, &beta;<sub>1</sub>." >This is incorrect. The true slope has no uncertainty as such</opt>
<opt text="The uncertainty of using a sample to estimate &beta;<sub>1</sub>."correct="true">Best student ever!</opt>
<opt text="The true standard deviation of  &beta;<sub>1</sub>'s normal distribution.">This is not correct.</opt>
</choice>

</exercise>

<exercise id="8" title="Draw x vs y">
The goal here is produce a plot like this :

<div style="text-align:center">
    <img src="./visual_representation.png"
    alt="Visual representation of the data generates in this example"
    width="40%">
</div>

- Create a new dataframe called `df_new` having the columns ['TV' and 'sales'].
- Plot the data in a graphic of TV and sales.

<codeblock id="02_01">---Hints---</codeblock>

</exercise>

<exercise id="9" title="Estimate the Linear Model">

- Guess &beta;<sub>0</sub> and &beta;<sub>1</sub> and make predictions with your model.
- Calculate the MSE for your model.

<codeblock id="02_02">---Hints---</codeblock>

</exercise>

<exercise id="10" title="Analize the MSE">

- Set beta0 = 2.2 and examine all models for beta1 = 0,3 in increments of 0.1

<codeblock id="02_03">---Hints---</codeblock>

</exercise>
