# STATICS-MPA03.01.04 (Combined)

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

![STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled.png](STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled.png)

**Part a) set x and y axes parallel and perpendicular to the force's axis:**

![STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%201.png](STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%201.png)

What is the length of the moment arm (d) for $\overrightarrow{F}$?  ________$\text{m}$

What is the magnitude and sense of the moment of the force about point O?  Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$  

**Part B) set x and y axes parallel and perpendicular to the rod's axis:**

![STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%202.png](STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%202.png)

What is the length of the moment arm for $F_{y}$?  ________ m

What is the magnitude and sense of the moment of the force about point O?

Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$ 

**Part C) use the universal set of x and y axes and decompose the force and the rod's length:**

![STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%203.png](STATICS-MPA03%2001%2004%20(Combined)%2029d55746ec964229bd669c21cbe8dda0/Untitled%203.png)

What is the length of the moment arm for $F_x$?  ________ m

What is the length of the moment arm for $F_y$?  ________ m

What is the magnitude and sense of the moment of the force about point O? Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{kN}\cdot\text{m}$  

### Variable Parameters

$[A]:$ Range (5, 10), in steps of 1

$[B]:$ Range (5, 10), in steps of 1

$[D]: [B]\times\sin(22.5^\circ)$

$[M]: [A]\times [D]$

$[Y]: [Y]= [A]\times\sin(22.5^\circ)$

$[U]: [U]= [B]\times\cos(22.5^\circ)$

$[V]: [V]= [B]\times\sin(22.5^\circ)$

$[E]: [E]= [A]\times\cos(45^\circ)$

$[F]: [F]= [A]\times\sin(45^\circ)$

  

# Answer:

a) $[D], [M]$

b) $[B], [M]$

b) $[V],[U], [M]$

# Feedback:

In this question, the force $\overrightarrow{F}$ is not perpendicular to the position vector $\overrightarrow{r}$, thus, one **CANNOT** use $|\overrightarrow{r}|$ directly as the moment arm to calculate the moment in $|\overrightarrow{M}|=|\overrightarrow{F}| |\overrightarrow{r}|$

Three different scalar methods can be used to solve this problem:

1. set x and y axes parallel and perpendicular to the **force's** axis, and then find the perpendicular distance from O to the line of action of the force.  Then you can use $|\overrightarrow{M}|=|\overrightarrow{F}| d$  
2. set x and y axes parallel and perpendicular to the **rod's** axis, and then $|\overrightarrow{M}|= F_yd$ , where d is the length of the rod, and $F_y$ is the component of $\overrightarrow{F}$ that is perpendicular to the rod.
3. use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$  (just be careful about the sign of the result).  In this example, for instance, all the components are positive.  You should get a net positive result i.e. a CCW rotation, because the term $F_yd_x$ creates a larger positive moment than the negative moment created by the term $-F_xd_y$.

**Part a)**

In part a), the axes are set based on the force's axis. Therefore, we can decompose the length of the rod to find the moment arm which is the perpendicular distance from point O to the line of action of the force.

$$d=|\overrightarrow{r}|\sin(22.5^\circ)=[D]~\text{m}$$

Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=|\overrightarrow{F}| d=([A]~\text{kN})([D]~\text{m})=[M]~\text{kN}\cdot\text{m} $$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CCW or   $+[M]~\text{kN}\cdot\text{m}$.

**Part b)**

In part b), the axes are set based on the rod's axis. Therefore, we can decompose the force into its x and y components. Here, $F_x$ produces no moment about point O since its line of action passes through this point. Therefore,

$$F_y=([A] ~\text{kN})\sin(22.5^\circ)=[Y]~\text{kN}$$

Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=F_y |\overrightarrow{r}|=([Y]~\text{kN})([B]~\text{m})=[M]~\text{kN}\cdot\text{m} $$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CCW or   $+[M]~\text{kN}\cdot\text{m}$.

**Part c)**

In part c), use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  

$$d_x=([B]~\text{m})\cos(22.5^\circ)=[U]~\text{m}$$

$$d_y=([B]~\text{m})\sin(22.5^\circ)=[V]~\text{m}$$

$$F_x=([A]~\text{kN})\cos(45^\circ)=[E]~\text{kN}$$

$$F_y=([A]~\text{kN})\sin(45^\circ)=[F]~\text{kN}$$

Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$. This formula considers CCW rotation as positive and can be used consistently as long as you substitute the parameters with correct signs.  In this example, for instance, all the components are positive.  You should get a net positive result i.e. a CCW rotation, because the term $F_yd_x$ creates a larger positive moment than the negative moment created by the term $-F_xd_y$

$$\curvearrowleft+|\overrightarrow{M}|=F_y d_x-F_xd_y= [F]([U])-[E]([V])=[M]\text{kN}\cdot\text{m}$$

Thus, the answer to this question is $[M]~\text{kN}\cdot\text{m}$, CCW or   $+[M]~\text{kN}\cdot\text{m}$.