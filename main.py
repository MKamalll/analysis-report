import pandas as pd
import numpy as np
import statsmodels as sm
import scipy
import matplotlib as plt
import pymc as pm

def somefunc():
    global var
    var = "Kamal"
    print(var)

print("Hello")

somefunc()
print(var)

del var