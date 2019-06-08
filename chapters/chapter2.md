---
title: 'Chapter 2: Day 1 afternoon, Introduction to Linear Regression'
description:
  '' 
prev: null
next: /chapter3/
type: chapter
id: 2
---

<exercise id="1" title="Linear Regression Basics" type="slides">
    <slides source="chapter2_01_introduction"></slides>
</exercise>

 
<exercise id="2" title="Getting Started">
    What does the estimated standard error of $\hat{\beta_1}$ represent?     
<choice>
<opt text="The standard deviation of the residuals ε.">This is not correct</opt>
<opt text="The uncertainty of the true slope,  β1." >This is incorrect. The true slope has no uncertainty as such</opt>
<opt text="The uncertainty of using a sample to estimate β1."correct="true">Best student ever!</opt>
<opt text="The true standard deviation of  β1's normal distribution.">This is not correct.</opt>

</choice>

</exercise>

<exercise id="3" title="Describe your data">

- Load data from data file `data.csv` using pandas
- Examine the `DataFrame`. How many points?

<codeblock id="01_03"> 
pandas read csv file data go to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
<br> 
A great method to describe the dataframe is .describe() 
</codeblock>

</exercise>

<exercise id="4" title="Draw x vs y">
The goal here is produce a plot like this 
<!--
<img src='ch1_fig1.png' width="50" height="60">
-->


- Rename the columns of your Data Frame.
- Plot the data in a graphic of x vs y.

<codeblock id="01_04">---Hints---</codeblock>

</exercise>

<exercise id="5" title="Estimate the Linear Model">

- Guess beta0 and beta1 and make predictions with your model.
- Calculate the MSE for your model.

<codeblock id="01_05">---Hints---</codeblock>

</exercise>

<exercise id="6" title="Analize the MSE">

- Set beta0 = 2.2 and examine all models for beta1 = 0,3 in increments of 0.1

<codeblock id="01_06">---Hints---</codeblock>

</exercise>

<exercise id="7" title="More to Do PPP">

<codeblock id="01_07">---Hints---</codeblock>

</exercise>