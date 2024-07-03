# OLS-Regression
"This repository contains the implementation of the Ordinary Least Squares (OLS) algorithm for linear regression. Includes code, documentation, and examples for using OLS to estimate model parameters and minimize prediction error."

# Ordinary Least Square

# importing library
import numpy as np

# creating an array 
x=np.array([1,3,5])
y=np.array([4.8,12.4,15.5])

# using mathematical formula for finding the  best parameters

# Calculating the value of w1
w1=((x*y).mean()-x.mean()*y.mean()) / ((x**2).mean()-(x.mean())**2)

# Final value of w1 
w1= 2.6750000000000003

# Calculating the value of w1
w0=y.mean()-w1*x.mean()

# Final value of w1
w0= 2.875
