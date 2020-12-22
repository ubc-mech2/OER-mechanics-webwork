# STATICS-MPA08.03.03

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
Sig Fig: Exact Integer
Status: Approved
Sub-Outcome: 3. any plane
Sub-Outcome Code: https://www.notion.so/STATICS-MPA08-03-0b9010fb5378488fb9e153157c7fe810
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Given $\overrightarrow{F}=(2\hat{i}+0\hat{j}-1\hat{k})~\text{N}$, and $\overrightarrow{r}_{OA}=(2\hat{i}+0\hat{j}+2\hat{k})~\text{m}$, determine the moment produced by the force $\overrightarrow{F}$ about point O. Express the result as a Cartesian vector.

Enter your answer:     $($___$\hat{i}~~-$___$~\hat{j}~~+~$___$\hat{k})$  $\text{N}\cdot\text{m}$

![STATICS-MPA08%2003%2003%20611ca6e0b4e841ca926cee66c3db5ce1/Untitled.png](STATICS-MPA08%2003%2003%20611ca6e0b4e841ca926cee66c3db5ce1/Untitled.png)

# Answer:

$0,-6,0$

# Feedback:

The moment of a force $\overrightarrow{F}$ about point O can be expressed using the vector cross product, namely,

$$\overrightarrow{M_O}=\overrightarrow{r}\times\overrightarrow{F}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\\\end{vmatrix}$$

$$=(r_yF_z-r_zF_y)\hat{i}-(r_xF_z-r_zF_x)\hat{j}+(r_xF_y-r_yF_x)\hat{k}$$

Thus, for this question:

$$\overrightarrow{M_O}=\overrightarrow{r_{OA}}\times\overrightarrow{F}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\ 2&0&2\\ 2&0&-1 \\\end{vmatrix}$$

$$=\{0(-1)-2(0)\}\hat{i}-\{2(-1)-2(2)\}\hat{j}+\{2(0)-0(2)\}\hat{k}$$

$$=\{0\hat{i}-(-6)\hat{j}+0\hat{k}\}~\text{N}\cdot\text{m}$$