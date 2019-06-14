---
title: 'Chapter 4: Introduction to Feed Forward'
description: 'Day 5 afternoon A.'
prev: /chapter3/
next: /chapter4/
id: 4
type: chapter
---

<exercise id="11" title="Feed forward Basics" type="slides">
    <slides source="chapter4_01_introduction"></slides>
</exercise>

<exercise id="12" title="Getting Started">

The number of nodes in the input layer is 10 and the hidden layer is 3. The maximum number of connections from the input layer to the hidden layer are?

<choice>
<opt text="30">This is not correct</opt>
<opt text="Less than 30" >This is incorrect. The true slope has no uncertainty as such</opt>
<opt text="More than 30"correct="true">Best student ever!</opt>
<opt text="Arbitrary value">This is not correct.</opt>
</choice>

</exercise>

<exercise id="13" title="Simple Neural Network">
The goal here is produce a simple neural network that can predict a step function like this one :

<div style="text-align:center">
    <img src="/chapter4/Figure_1.png"
    alt="Visual representation of the data generates in this example"
    width="50%">
</div>

- Create a keras model called `model` with one hidden layer with a single node.
- Plot the predicted values against the input variable `x`

<codeblock id="04_01">---Hints---</codeblock>

</exercise>

<exercise id="14" title="Simple Neural Network II">
The goal here is produce a simple neural network that can predict a function like this one :

<div style="text-align:center">
    <img src="/chapter4/Figure_2.png"
    alt="Visual representation of the data generates in this example"
    width="50%">
</div>

- Build a keras model called `model` with one hidden layer with two nodes.
- Plot the predicted values against the input variable `x`

<codeblock id="04_02">---Hints---</codeblock>

</exercise>

<exercise id="15" title="Simple Neural Network III">
The goal here is produce a simple neural network that can predict a function like this one :

<div style="text-align:center">
    <img src="/chapter4/Figure_3.png"
    alt="Visual representation of the data generates in this example"
    width="50%">
</div>


- Build a keras model called `model` with one hidden layer with four nodes.
- Plot the predicted values against the input variable `x`

<codeblock id="04_03">---Hints---</codeblock>

</exercise>
