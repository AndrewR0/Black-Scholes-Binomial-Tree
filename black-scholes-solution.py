'''
Induction: 
The purpose of this project is to use a binomial tree more realistically than what was done for the earlier homework
assignment. That is to make a tree with many more nodes and to notice the improvements to the error that result
from more nodes. You may use any programming language you want, or even do it in excel, but you must include
your code/screen shots of excel commands with your answers to the questions at the end of the project.
'''

import numpy as np
from scipy.stats import norm

# European Option Prices according to the Black-Scholes solution
# ---------------------------------------------------
S0 = 10 # current stock price
K = 10 # strike price of option
r = 0.02 # constant risk-free interest rate
sigma = 0.25 # constant volatility of the stock price
T = 0.25 # time to maturity

phi = norm.cdf

def call_option(S0: float, K: float, r: float, sigma:float, T:float):
    d1 = (np.log(S0/K) + (r + (sigma**2)/2)*T)/sigma*np.sqrt(T)
    d2 = d1 - sigma*np.sqrt(T)
    return S0 * phi(d1) - K * np.exp(-r * T) * phi(d2)



# Binomail Model
# --------------

