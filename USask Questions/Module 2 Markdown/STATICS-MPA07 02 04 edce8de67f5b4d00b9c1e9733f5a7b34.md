# STATICS-MPA07.02.04

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
Sub-Outcome: 2. the determinant expansion
Sub-Outcome Code: https://www.notion.so/STATICS-MPA07-02-ad99417e7f97404a815b4e638935d21d
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Determining the moment about point O in a 3D problem requires taking the cross product between a position vector depicting the moment arm, and the force vector. If each vector is depicted in Cartesian coordinates as such:

$$\overrightarrow{F}=F_x\hat{i}+F_y\hat{j}+F_z\hat{k}\\\overrightarrow{r}=r_x\hat{i}+r_y\hat{j}+r_z\hat{k}$$

then select the correct representation of the determinant expansion of the vector moment calculation:

a) $\overrightarrow{M}_O=(r_yF_z-r_zF_y)\hat{i}-(r_xF_z-r_zF_x)\hat{j}+(r_xF_y-r_yF_x)\hat{k}$

b) $\overrightarrow{M}_O=(r_yF_z-r_zF_y){i}-(r_xF_z-r_zF_x){j}+(r_xF_y-r_yF_x){k}$

c) $\overrightarrow{M}_O=(F_yr_z-F_zr_y)\hat{i}-(F_xr_z-F_zr_x) \hat{j}+(F_xr_y-F_yr_x)\hat{k}$

d) $\overrightarrow{M}_O=(r_yF_z+r_zF_y)\hat{i}-(r_xF_z+r_zF_x)\hat{j}+(r_xF_y+r_yF_x)\hat{k}$

# Answer:

a) $\overrightarrow{M}_O=(r_yF_z-r_zF_y)\hat{i}-(r_xF_z-r_zF_x)\hat{j}+(r_xF_y-r_yF_x)\hat{k}$

# Feedback:

a) Well done! Even though the force vector $\overrightarrow{F}$ is stated before the position vector $\overrightarrow{r}$, the order of the determinant doesn't change ($\overrightarrow{r}\times\overrightarrow{F}$). Consider the pattern for calculating a 3D determinant in the diagram below:

![STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png](STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png)

This option shows the correct order of terms! Remember the negative sign in front of the $\hat{j}$ term in the middle.

---

b) While the order and pattern of terms in this option is correct, it’s missing the correct vector notation on the unit vectors (hats on top of the variables). Consider the pattern for calculating a 3D determinant in the diagram below:

![STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png](STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png)

Notice how each unit vector has the hat on top (i.e. $\hat{i}$ as opposed to $i$). This vector notation is important for presentation of a vector moment. 

---

c) This option would be correct if the determinant was set up for $\overrightarrow{F}\times\overrightarrow{r}$. However, the moment about a point is always calculated as $\overrightarrow{r}\times\overrightarrow{F}$. To calculate the correct moment, consider the pattern for calculating a 3D determinant in the diagram below:

![STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png](STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png)

The y & z components are paired with the $\hat{i}$ term, the x & z components with the $\hat{j}$ term, and the x & y components with the $\hat{k}$ term.

---

d) Close! Remember that calculating the 2D determinant requires **subtracting** the second product from the first, so each sign inside the brackets should be a **negative** sign. Consider the pattern for calculating a 3D determinant in the diagram below:

![STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png](STATICS-MPA07%2002%2004%20edce8de67f5b4d00b9c1e9733f5a7b34/Untitled.png)

Also notice the negative sign in front of the $\hat{j}$ term. All the negative signs are important in this expanded representation!

---