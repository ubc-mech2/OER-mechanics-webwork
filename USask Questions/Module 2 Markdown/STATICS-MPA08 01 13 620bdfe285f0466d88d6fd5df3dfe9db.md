# STATICS-MPA08.01.13

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
Randomizable Parameters: No
Sean Reviewed: Yes
Shaobo Reviewed: No
Sig Fig: Exact
Status: Approved
Sub-Outcome: 1. all 8 octants
Sub-Outcome Code: https://www.notion.so/STATICS-MPA08-01-52fdd412aa704056b70ae01ab06250b1
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Given $\overrightarrow{F}_{DA}=(-8\hat{i}+6\hat{j}-2\hat{k})~\text{kN}$, and $\overrightarrow{r_{PD}}=(0\hat{i}+0\hat{j}+4\hat{k})~\text{m}$, determine the moment produced by the force $\overrightarrow{F}_{DA}$ about **point P**. Express the result as a Cartesian vector.

Enter your answer:     $($___$\hat{i}~~-$___$~\hat{j}~~+~$___$\hat{k})$  $\text{kN}\cdot\text{m}$

![STATICS-MPA08%2001%2013%20620bdfe285f0466d88d6fd5df3dfe9db/Untitled.png](STATICS-MPA08%2001%2013%20620bdfe285f0466d88d6fd5df3dfe9db/Untitled.png)

# Answer:

$-24,32,0$

# Feedback：

The moment of a force $\overrightarrow{F}$ about point O can be expressed using the vector cross product, namely,

$$\overrightarrow{M_O}=\overrightarrow{r}\times\overrightarrow{F}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\\\end{vmatrix}$$

$$=(r_yF_z-r_zF_y)\hat{i}-(r_xF_z-r_zF_x)\hat{j}+(r_xF_y-r_yF_x)\hat{k}$$

Thus, for this question:

$$\overrightarrow{M_P}=\overrightarrow{r}_{PD}\times\overrightarrow{F}_{DA}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\ 0&0&4\\ -8&6&-2\\\end{vmatrix}$$

$$=\{0(-2)-4(6)\}\hat{i}-\{0(-2)-4(-8)\}\hat{j}+\{0(6)-0(-8)\}\hat{k}$$

$$=\{-24\hat{i}-32\hat{j}+0\hat{k}\}~\text{kN}\cdot\text{m}$$