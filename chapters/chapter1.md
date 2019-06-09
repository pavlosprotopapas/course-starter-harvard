---
title: 'Chapter 1: Introduction to Regression.'
description: 'Day 1 morning A.'
prev: null
next: /chapter2/
id: 1
type: chapter
---

<exercise id="1" title="Regression Basics" type="slides">
    <slides source="chapter1_01_introduction"></slides>
</exercise>

<exercise id="2" title="Getting Started">

Is it possible for R<sup>2</sup> for a model to be negative? : 

<choice>
<opt text="No, R<sup>2</sup> cannot be negative">This is not correct.</opt>
<opt text="Yes, if the predictor in a least-squares regression model is poor." correct="true">Good job!</opt>
<opt text="Yes, if the predictor is negatively correlated with the response.">This is not correct.</opt>
<opt text="Yes, if the model does worse than using <bar>Y</bar> for all predictions">This is not correct.</opt>
</choice>

</exercise>

<exercise id="3" title="Describe your data.">

- Load data from data file `data.csv` using pandas.
- Examine the `DataFrame`. How many points and how many columns are there?

<codeblock id="01_03"> 

- Help for pandas __[read csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)__.

- A great method to describe the dataframe is `.describe()`.

</codeblock>

</exercise>

<exercise id="4" title="Draw TV vs Sales for a subset of data">

- Here we select just 12 points, the columns TV and sales.
- Lets plot TV-budget vs sales like in lecture. 

<codeblock id="01_04">

- Help for __[matplotlib](https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html)__.

</codeblock>

</exercise>

<exercise id="5" title="Nearest neighbors">
Use the code provided to find the nearest neighbors and plot the value of y at various x's. This should produce a similar plot to k=1 nearest neighbor shown in class. 

<codeblock id="01_05">

Help for __[idxmin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmin.html)__.

</codeblock>

</exercise>