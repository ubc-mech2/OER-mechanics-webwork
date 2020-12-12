# STATICS-MPA03.01.03 (Combined)

Automatic Grading: Yes
Keywords: moment, moment arm
Last Edit: Oct 30, 2020 11:22 AM
Last Edited By: Nicholas Betancourt
Learning Outcome: Determine the magnitude and sense of a 2D moment using multiple scalar methods, given different information in the problem diagram/statement
Margin of Error: 0.1
Module: Module 2: Identify and solve introductory level rigid body statics problems
Needs Calculator: No
On Mobius: Yes
Origin/Author: Zoe
Question Format: Numerical fill in the blank
Question Type: A
Randomizable Parameters: No
Sean Reviewed: Yes
Shaobo Reviewed: No
Sig Fig: 3 sig figs
Status: Approved
Sub-Outcome: 1. M=Fd  (use problems where you can see all 3 different ways) have + and - moments e.g. in text Ex 4.5 and 4.6
Sub-Outcome Code: https://www.notion.so/STATICS-MPA03-01-4d37234aacf14de5b96458b6bce2263c
Topic/ Unit: 2. Calculate the moment of a force about a point or an axis in 2D and 3D using vector and scalar formulations (MPA)

# Question:

Given the magnitude of $\overrightarrow{F}$ is $[A]$ kN and the magnitude of $\overrightarrow{r}$ is $[B]$ m , determine the magnitude and sense of the moment of $\overrightarrow{F}$about point O using the following scalar methods.  Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

![STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled.png](STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled.png)

**Part a) set x and y axes parallel and perpendicular to the force's axis:**

![STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%201.png](STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%201.png)

What is the length of the moment arm (d) for $\overrightarrow{F}$?  ________$\text{m}$

What is the magnitude and sense of the moment of the force about point O?  Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$  

**Part B) set x and y axes parallel and perpendicular to the rod's axis:**

![STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%202.png](STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%202.png)

What is the length of the moment arm for $F_{y}$?  ________ m

What is the magnitude and sense of the moment of the force about point O?

Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$ 

**Part C) use the universal set of x and y axes and decompose the force and the rod's length:**

![STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%203.png](STATICS-MPA03%2001%2003%20(Combined)%20b3146a9c8f894ff6ae2a02788699d69a/Untitled%203.png)

What is the length of the moment arm for $F_x$?  ________ m

What is the length of the moment arm for $F_y$?  ________ m

What is the magnitude and sense of the moment of the force about point O? Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$  

### Variable Parameters

$[A]:$ Range (5, 10), in steps of 1

$[B]:$ Range (5, 10), in steps of 1

$[D]: [B]\times\sin(35^\circ)$

$[M]: [A]\times [D]$

$[Y]: [Y]= [A]\times\sin(35^\circ)$

$[U]: [U]= [B]\times\cos(25^\circ)$

$[V]: [V]= [B]\times\sin(25^\circ)$

$[E]: [E]= [A]\times\sin(30^\circ)$

$[F]: [F]= [A]\times\cos(30^\circ)$

  

# Answer:

a) $[D], -[M]$

b) $[B], -[M]$

b) $[V],[U], -[M]$

# Feedback:

In this question, the force $\overrightarrow{F}$ is not perpendicular to the position vector $\overrightarrow{r}$, thus, one **CANNOT** use $|\overrightarrow{r}|$ directly as the moment arm to calculate the moment in $|\overrightarrow{M}|=|\overrightarrow{F}| |\overrightarrow{r}|$

Three different scalar methods can be used to solve this problem:

1. set x and y axes parallel and perpendicular to the **force's** axis, and then find the perpendicular distance from O to the line of action of the force.  Then you can use $|\overrightarrow{M}|=|\overrightarrow{F}| d$  
2. set x and y axes parallel and perpendicular to the **rod's** axis, and then $|\overrightarrow{M}|= F_yd$ , where d is the length of the rod, and $F_y$ is the component of $\overrightarrow{F}$ that is perpendicular to the rod.
3. use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$  (just be careful about the sign of the result).  In this example, for instance, you should get a net negative result i.e. a CW rotation, as a result of $F_y$ being a negative value (since $F_y$ points down).  However, note that $d_y$ is also negative i.e. the $-F_xd_y$ term creates a positive moment.  

**Part a)**

In part a), the axes are set based on the force's axis. Therefore, we can decompose the length of the rod to find the moment arm which is the perpendicular distance from point O to the line of action of the force.

$$d=|\overrightarrow{r}|\sin(35^\circ)=[D]~\text{m}$$

Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=-|\overrightarrow{F}| d=-([A]~\text{kN})([D]~\text{m})=-[M]~\text{kN}\cdot\text{m} $$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CW or -  $[M]~\text{kN}\cdot\text{m}$.

**Part b)**

In part b), the axes are set based on the rod's axis. Therefore, we can decompose the force into its x and y components. Here, $F_x$ produces no moment about point O since its line of action passes through this point. Therefore,

$$F_y=([A] ~\text{kN})\sin(35^\circ)=[Y]~\text{kN}$$

Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=-F_y |\overrightarrow{r}|=-([Y]~\text{kN})([B]~\text{m})=-[M]~\text{kN}\cdot\text{m} $$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CW or -  $[M]~\text{kN}\cdot\text{m}$.

**Part c)**

In part c), use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  

$$d_x=([B]~\text{m})\cos(25^\circ)=[U]~\text{m}$$

$$d_y=-([B]~\text{m})\sin(25^\circ)=-[V]~\text{m}$$

$$F_x=([A]~\text{kN})\sin(30^\circ)=[E]~\text{kN}$$

$$F_y=-([A]~\text{kN})\cos(30^\circ)=-[F]~\text{kN}$$

Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$. This formula considers CCW rotation as positive and can be used consistently as long as you substitute the parameters with correct signs. For example, $F_y$  is pointing down in this case. Combined with a positive moment arm $d_x$, it causes a CW rotation about point O. So when you substitute a negative $F_y$ and a positive $d_x$ into the formula, the result is negative, which indicates the force $F_y$ yields a CW rotation. Similarly, note that $d_y$ is also negative, i.e. the $-F_xd_y$ term creates a positive moment, which means the rotation is CCW.  

$$\curvearrowleft+|\overrightarrow{M}|=F_y d_x-F_xd_y= -[F]([U])-[E](-[V])=-[M]\text{kN}\cdot\text{m}$$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CW or -  $[M]~\text{kN}\cdot\text{m}$.