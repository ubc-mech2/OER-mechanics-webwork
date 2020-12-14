# STATICS-MPA03.01.02 (Combined)

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

Given the magnitude of $\overrightarrow{F}_B$ is $[A]$ lb, determine the magnitude and sense of the moment of $\overrightarrow{F}_B$about point A using the following scalar methods.  Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

![STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled.png](STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled.png)

**Part a) set x and y axes parallel and perpendicular to the force's axis:**

![STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%201.png](STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%201.png)

What is the length of the moment arm (d) for $\overrightarrow{F}_B$?  ________ $\text{ft}$

What is the magnitude and sense of the moment of the force about point A?  Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{lb}\cdot\text{ft}$  

**Part B) set x and y axes parallel and perpendicular to the rod's axis:**

![STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%202.png](STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%202.png)

What is the length of the moment arm for $F_{By}$?  ________ $\text{ft}$

What is the magnitude and sense of the moment of the force about point A?

Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{lb}\cdot\text{ft}$ 

**Part C) use the universal set of x and y axes and decompose the force and the rod's length:**

![STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%203.png](STATICS-MPA03%2001%2002%20(Combined)%20ac9dfbd2d70d496fb387298459a73c4f/Untitled%203.png)

What is the length of the moment arm for $F_{Bx}$?  ________ $\text{ft}$

What is the length of the moment arm for $F_{By}$?  ________ $\text{ft}$

What is the magnitude and sense of the moment of the force about point A? Express the sense of the moment with a + or - sign in front of your answer, where + is for CCW and - is for CW.

 ________ $\text{lb}\cdot\text{ft}$  

### Variable Parameters

$[A]:$ Range (5, 10), in steps of 1

$[M]: [A]\times2.27$

$[Y]: [Y]= [A]\times\cos(25^\circ)$

$[E]: [E]= [A]\times\sin(5^\circ)$

$[F]: [F]= [A]\times\cos(5^\circ)$

  

# Answer:

a) $2.27, [M]$

b) $2.5, [M]$

b) $0.855,2.35, [M]$

# Feedback:

In this question, the force $\overrightarrow{F}_B$ is not perpendicular to the rod, thus, one **CANNOT** use the length of the rod directly as the moment arm to calculate the moment in $|\overrightarrow{M}|=|\overrightarrow{F}|( 2.5~\text{ft})$

Three different scalar methods can be used to solve this problem:

1. set x and y axes parallel and perpendicular to the **force's** axis, and then find the perpendicular distance from O to the line of action of the force.  Then you can use $|\overrightarrow{M}|=|\overrightarrow{F}| d$  
2. set x and y axes parallel and perpendicular to the **rod's** axis, and then $|\overrightarrow{M}|= F_yd$ , where d is the length of the rod, and $F_y$ is the component of $\overrightarrow{F}$ that is perpendicular to the rod.
3. use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$  (just be careful about the sign of the result).  

**Part a)**

In part a), the axes are set based on the force's axis. Therefore, we can decompose the length of the rod to find the moment arm which is the perpendicular distance from point O to the line of action of the force.

$$d=(2.5~\text{ft})\sin(65^\circ)=2.27~\text{ft}$$

Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=|\overrightarrow{F}| d=([A]~\text{lb})(2.27~\text{ft})=[M]~\text{lb}\cdot\text{ft} $$

Thus, the answer to this question is $[M]~\text{lb}\cdot\text{ft}$, CCW or + $[M]~\text{lb}\cdot\text{ft}$.

**Part b)**

In part b), the axes are set based on the rod's axis. Therefore, we can decompose the force into its x and y components. Here, $F_x$ produces no moment about point A since its line of action passes through this point. Therefore,

$$F_y=([A] ~\text{lb})\cos(25^\circ)=[Y]~\text{lb}$$

Then the length of the rod, 2.5 $\text{ft}$, is the moment arm for $F_y$. Considering counterclockwise moments as positive, and applying the principle of moments, we have

$$\curvearrowleft+|\overrightarrow{M}|=([Y]~\text{kN})(2.5~\text{ft})=[M]~\text{lb}\cdot\text{ft} $$

Thus, the answer to this question is $[M]~\text{lb}\cdot\text{ft}$, CCW or + $[M]~\text{lb}\cdot\text{ft}$.

**Part c)**

In part c), use the universal set of x and y axes (up/down, left/right) and decompose the force into $F_x$ and $F_y$, and the rod's length into $d_x$ and $d_y$.  

$$d_x=(2.5~\text{ft})\cos(20^\circ)=2.35~\text{ft}$$

$$d_y=(2.5~\text{ft})\sin(20^\circ)=0.855~\text{ft}$$

$$F_x=([A]~\text{lb})\sin(5^\circ)=[E]~\text{lb}$$

$$F_y=([A]~\text{lb})\cos(5^\circ)=[F]~\text{lb}$$

Then use the formula $|\overrightarrow{M}|=F_yd_x-F_xd_y$. This formula considers CCW rotation as positive and can be used consistently as long as you substitute the parameters with correct signs. For example, $F_y$  is pointing up in this case. Combined with a positive moment arm $d_x$, it causes a CCW rotation about point A. So when you substitute a positive $F_y$ and a positive $d_x$ into the formula, the result is positive, which indicates the force $F_y$ yields a CCW rotation. 

$$\curvearrowleft+|\overrightarrow{M}|=F_y d_x-F_xd_y= [F](2.35~\text{ft})-[E](0.855~\text{ft})=[M]\text{kN}\cdot\text{m}$$

Thus, the answer to this question is $[M]~\text{lb}\cdot\text{ft}$, CCW or + $[M]~\text{lb}\cdot\text{ft}$.