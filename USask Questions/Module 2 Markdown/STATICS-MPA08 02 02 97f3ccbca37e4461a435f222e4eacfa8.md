# STATICS-MPA08.02.02

Automatic Grading: Yes
Keywords: 3D, cross product, moment
Last Edit: Oct 30, 2020 11:22 AM
Last Edited By: Nicholas Betancourt
Learning Outcome: Calculate the vector moment of a force about a point in 3D, given a Cartesian force vector and a Cartesian position vector (text and diagram)
Margin of Error: 0
Module: Module 2: Identify and solve introductory level rigid body statics problems
Needs Calculator: No
On Mobius: Yes
Origin/Author: Zoe
Question Format: Numerical fill in the blank
Question Type: A
Randomizable Parameters: Yes
Sean Reviewed: Yes
Shaobo Reviewed: No
Sig Fig: Exact
Status: Approved
Sub-Outcome: 2. forces along any axis
Sub-Outcome Code: https://www.notion.so/STATICS-MPA08-02-c6f23728f1f349399ce4b09e62800646
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Given $\overrightarrow{F_1}=(0\hat{i}-60\hat{j}+0\hat{k})~\text{lb}$, and $\overrightarrow{r}_{OA}=(0\hat{i}+2\hat{j}+2\hat{k})~\text{ft}$, determine the moment produced by the force $\overrightarrow{F}_{1}$ about **point O**. Express the result as a Cartesian vector.

Enter your answer:     $($___$\hat{i}~~-$___$~\hat{j}~~+~$___$\hat{k})$  $\text{lb}\cdot\text{ft}$

![STATICS-MPA08%2002%2002%2097f3ccbca37e4461a435f222e4eacfa8/Untitled.png](STATICS-MPA08%2002%2002%2097f3ccbca37e4461a435f222e4eacfa8/Untitled.png)

# Answer:

$120,0,0$

# Feedback:

The moment of a force $\overrightarrow{F}$ about point O can be expressed using the vector cross product, namely,

$$\overrightarrow{M_O}=\overrightarrow{r}\times\overrightarrow{F}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\\\end{vmatrix}$$

$$=(r_yF_z-r_zF_y)\hat{i}-(r_xF_z-r_zF_x)\hat{j}+(r_xF_y-r_yF_x)\hat{k}$$

Thus, for this question:

$$\overrightarrow{M_O}=\overrightarrow{r}_{OA}\times\overrightarrow{F}_1=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\ 0&2&2\\ 0&-60&0\\\end{vmatrix}$$

$$=\{2(0)-2(-60)\}\hat{i}-\{0(0)-2(0)\}\hat{j}+\{0(-60)-2(0)\}\hat{k}$$

$$=\{120\hat{i}-0\hat{j}+0\hat{k}\}~\text{lb}\cdot\text{ft}$$