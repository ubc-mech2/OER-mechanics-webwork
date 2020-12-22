# STATICS-MPA07.01.03

Automatic Grading: Yes
Last Edit: Oct 30, 2020 11:22 AM
Last Edited By: Nicholas Betancourt
Learning Outcome: Recognize the determinant form of the vector moment calculation for a force about a point in 3D, for Cartesian position and force vectors
Module: Module 2: Identify and solve introductory level rigid body statics problems
Needs Calculator: No
On Mobius: Yes
Origin/Author: Caelia
Question Format: Multiple choice
Question Type: A
Randomizable Parameters: No
Sean Reviewed: Yes
Shaobo Reviewed: No
Status: Approved
Sub-Outcome: 1. the determinant
Sub-Outcome Code: https://www.notion.so/STATICS-MPA07-01-8146e6f27aec4474aa257073463d0020
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Determining the moment about point O in a 3D problem requires taking the cross product between a position vector depicting the moment arm, and the force vector. If each vector is expressed in Cartesian coordinates as such:

$$\overrightarrow{r}=3\hat{i}+5\hat{j}-2\hat{k}\\\overrightarrow{F}=\hat{i}-9\hat{j}+3\hat{k}$$

then select the correct representation of the determinant form of the vector moment calculation:

a) $\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\3&5&-2\\1&-9&3\\\end{vmatrix}$

b) $\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\3&5&-2\\0&-9&3\\\end{vmatrix}$

c) $\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\3&5&2\\1&9&3\\\end{vmatrix}$

d) $\overrightarrow{M}_O=\begin{vmatrix}{i}&{j}&{k}\\3&5&-2\\1&-9&3\\\end{vmatrix}$

# Answer:

a) $\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\3&5&-2\\1&-9&3\\\end{vmatrix}$

# Feedback:

a) Correct! The determinant representing the vector formulation of the moment about point O comes from the cross product $\overrightarrow{r}\times\overrightarrow{F}$. We know that the determinant for the moment vector has three rows: the first made from the unit vectors, the second row is the position vector, and the third row is the force vector, with $xyz$ components placed from left to right. Remember that components that appear not to have coefficients are represented as a 1 in the matrix.  

b) Close! While the elements in this option are all in the correct place, the $x$ component of the force vector in the third row is not correct. When a component appears not to have a coefficient but the unit vector is present (in this case, $\hat{i}$), the correct number to use is 1. 

c) While the elements in this option are generally in the correct place, it is missing negative signs. Watch that any components with a negative sign are included when constructing the matrix for the determinant. 

d) While the elements in this option are generally in the correct place, the unit vector notation is missing in the first row (the hats on top of each variable). Proper vector notation is important, because the variable $i$ is different than the unit vector $\hat{i}$. The correct answer will have hats on the variables in the first row!