[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aAI3qcR2)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16122237&assignment_repo_type=AssignmentRepo)
# Homework 3 due Thursday Oct 3

HW3 – Exercise 5.21 modified: Gravitational field around a binary star system. 

Suppose we have two stars, and we want to calculate the resulting gravitational field (neglecting GR effects). 
One way to do this is to first calculate the gravitational potential $\phi$ and then take its gradient. 
For a point mass $M$ at the origin, the gravitational potential at a distance $r$ from the origin is 
$$\phi = G M/r,$$ where $G = 6.67259\times 10^{-8}$ $\mathrm{cm}^{3}\ \mathrm{g}^{-1}\ \mathrm{s}^{-2}$, and the gravitational field is $$g = −\nabla\phi.$$
The nice thing about scalar potentials is that they're additive, such that $\phi = \phi_1 + \phi_2$. 

a) Imagine you have two stars, of 1 $M_\odot$ (solar mass), in a binary with a separation of 1 AU (astronomical unit) apart. 
Now imagine we want to simulate these stars on a cartesian x-y grid co-moving with the binary (i.e. you can think of the stars as fixed points on the grid).
Calculate the resulting graviational potential on a 10 AU × 10 AU square plane which surrounds the stars and passes through them. Take the center of the plane to be the center of mass of the binary, and for consistency, take the binary to be aligned with the x-axis. Calculate the potential at 0.1 AU spaced points in a grid, and make a visualization in python using a 2D density map (there are many ways to do this; one suggestion would be to ues the function pcolormesh(x, y, 2Ddata); adding a color bar would also be helpful). 

Hint: First calculate the potential for each star, then add them together, noting that the distance away from either star is $r = \sqrt{(x \pm 0.5 AU)^2 + y^2}$ . Store the potential as a 2D array. 

b) Now for the differentiation part: Calculate the partial derivatives of the potential $\phi$ with respect to x and y, and hence find the gravitational field in the xy plane. Then, make a visualization of the field. This is a little trickier than visualizing the potential, because the gravitational field has both a magnitude and direction. The matplotlib functions quiver() or streamplot() may be useful here.

Hint: Find both the x and y components of the field independently and store them as 2 separate 2D arrays. When taking the derivative, most methods will do, so no need to use any fancy higher-order methods. Using central-difference or numpy.gradient will suffice.)


