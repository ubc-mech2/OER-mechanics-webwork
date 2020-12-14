# STATICS-VDP0X.X.X

Automatic Grading: Yes
Keywords: 3D, Dot product
Last Edit: Oct 30, 2020 11:22 AM
Last Edited By: Sean Maw
Margin of Error: 0.01
Needs Calculator: Yes
On Mobius: No
Origin/Author: Zoe
Question Format: Numerical fill in the blank
Question Type: A
Randomizable Parameters: Yes
Sean Reviewed: Yes
Shaobo Reviewed: No
Sig Fig: 3 sig figs
Status: Approved

# Question:

Given the components of two vectors, $\overrightarrow{A}=(\hat{[X]i}+[Y]\hat{j}+[Z]\hat{k})$ and $\overrightarrow{B}=(\hat{[O]i}+[P]\hat{j}+[Q]\hat{k})$. What is the angle between these two vectors? Round your answer to 3 significant figures.

Enter your answer: ____$^\circ$

### Variable Parameters

$[X]:$ Range (-8, 8) in steps of 2

$[Y]:$ Range (-8, 8) in steps of 2

$[Z]:$ Range (-8, 8) in steps of 2

$[O]:$ Range (-9, 9) in steps of 2

$[P]:$ Range (-9, 9) in steps of 2

$[Q]:$ Range (-9, 9) in steps of 2

# Answer:

$$\text{cos}^{-1}(\frac{[X][O]+[Y][P]+[Z][Q]}{\sqrt{[X]^2+[Y]^2+[Z]^2}\cdot \sqrt{[O]^2+[P]^2+[Q]^2}})$$

# Feedback:

The dot product of two vectors is given by:

$$⁍$$

Therefore, if the dot product of the two vectors and their magnitudes are known, we can calculate the angle between these two vectors using:

$$\theta=\text{cos}^{-1}(\frac{\overrightarrow{A}\cdot\overrightarrow{B}}{|\overrightarrow{A}||\overrightarrow{B}|})$$

In this question, the dot product and the magnitudes are not given directly. But the vector components are provided. Thus, the dot product of these two vectors can be calculated as:

$$\overrightarrow{A}\cdot\overrightarrow{B}=A_x\cdot B_x+A_y \cdot B_y+A_z\cdot B_z$$

Also the magnitudes of these vectors are:

$$|A|=\sqrt{{A_x}^2+{A_y}^2+{A_z}^2}$$

and,

$$|B|=\sqrt{{B_x}^2+{B_y}^2+{B_z}^2}$$