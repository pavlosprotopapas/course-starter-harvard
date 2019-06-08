---
title: 'Chapter 1: Day 1 morning A, Introduction to Regression'
description:
  '' 
prev: null
next: /Chapter 2/
type: chapter
id: 1
---

<exercise id="1" title="Regression Basics" type="slides">
    <slides source="chapter1_01_introduction"></slides>
</exercise>

 
<exercise id="2" title="Getting Started">

The Linear Regression Models are used for : 

<choice>
<opt text="Answer 1">This is not correct either.</opt>
<opt text="Approximate the dependency relationship between a dependent variable Y, the independent variables X." correct="true">Good job!</opt>
<opt text="Answer 3">This is not correct either.</opt>
</choice>

</exercise>


<exercise id="3" title="Describe your data">

- Load data from data file `data.csv` using pandas
- Examine the `DataFrame`. How many points and how many columns are there?

<codeblock id="01_03"> 
pandas read csv file data go to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
<br> 
A great method to describe the dataframe is .describe() 
</codeblock>

</exercise>

<exercise id="4" title="Draw TV-budget vs Sales for a subset of data">
Here we select just 12 points and select only the TV-budget and sales and plot one against the other like in lecture. 


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