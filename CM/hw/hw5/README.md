[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Cvh8eX_0)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16669314&assignment_repo_type=AssignmentRepo)
# HW5
Homework 5 due Tuesday Oct 24

**Exercises 7.4 and 7.6: Fourier filtering and smoothing/ Comparison of DFT and DCT**    


**Reminder: Exercise 7.4**

_This was done in class, and there are example solutions on Blackboard, which you are free to consult, but the code will be useful for 7.6_

In the on-line resources (http://www-personal.umich.edu/~mejn/cp/programs.html) you’ll find a file called dow.txt. It contains the daily closing value for each business day from late 2006 until the end of 2010 of the Dow Jones Industrial Average, which is a measure of average prices on the US stock market. Write a program to do the following:
    
    a) Read in the data from dow.txt and plot them on a graph.
    
    b) Calculate the coefficients of the discrete Fourier transform of the data using 
    the function rfft from numpy.fft, which produces an array of N/2 + 1 complex numbers.
    
    c) Now set all but the first 10% of the elements of this array to zero 
    (i.e., set the last 90% to zero but keep the values of the first 10%).
    
    d) Calculate the inverse Fourier transform of the resulting array, zeros and all, 
    using the function irfft, and plot it on the same graph as the original data. 
    You may need to vary the colors of the two curves to make sure they both show up on the graph. 
    Comment on what you see. What is happening when you set the Fourier coefficients to zero?
    
    e) Modify your program so that it sets all but the first 2% of the coefficients to zero and run it again.

**7.6 is new:**

Exercise 7.4 looked at data representing the variation of the Dow Jones Industrial Average, 
colloquially called “the Dow,” over time. That particular time period studied in that exercise 
was special in one sense: the value of the Dow at the end of the period was almost the same as 
at the start (due to the 2008 financial crisis), so the function was, roughly speaking, periodic. 
In the on-line resources there is another file called dow2.txt, which also contains data on the 
Dow but for a different time period, from 2004 until 2008. Over this period the value changed 
considerably from a starting level around 9000 to a final level around 14000.
    
    a) Write a program similar to the one for Exercise 7.4, part (e), in which you read 
    the data in the file dow2.txt and plot it on a graph. Then smooth the data by calculating 
    its Fourier transform, setting all but the first 2% of the coefficients to zero, and 
    inverting the transform again, plotting the result on the same graph as the original data. 
    
    As in Exercise 7.4 you should see that the data are smoothed, but now there will be an 
    additional artifact: at the beginning and end of the plot you should see large deviations 
    away from the true smoothed function. These occur because the function is required to 
    be periodic —its last value must be the same as its first— to make use of the DFT. 
    So, the transform needs to deviate substantially from the correct value to make the two ends 
    of the function meet. In some situations (including this one), this behavior is problematic. 
    If we want to use a Fourier transform for smoothing, we would  prefer that it not 
    introduce artifacts of this kind.
    
    b) Modify your program to repeat the same analysis using discrete cosine transforms. 
    You can use the functions from dcst.py to perform the transforms if you wish. Again, 
    discard all but the first 2% of the coefficients, invert the transform, and plot the result. 
    You should see a significant improvement, with less distortion of the function at the ends 
    of the interval. This occurs because, as discussed in class (see also the end of Section 7.3 
    in the textbook), the cosine transform does not force the value of the function to be the same 
    at both ends; it flips the values.

    c) Try different levels of smoothing (some suggestions are 10%, 2%, 1%, but you should play 
    around with it). Make a plot with the original data, and different levels of smoothing, where 
    it is visually distinguishable which line corresponds to which data/smoothing (through the use 
    of different colors, or different linestyles, or different y-axes, or some combination thereof).
    
    
For this exercise, let's use argparse (https://docs.python.org/3/library/argparse.html) to pass arguments to your code from the command line. 
**Write your code so it can be run on dow.txt or dow2.txt, keep the first 10% or 2% of Fourier coefficients, and use DFT or DCT.**
