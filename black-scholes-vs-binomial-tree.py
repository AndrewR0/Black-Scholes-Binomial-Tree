import numpy as np
from scipy.stats import norm

# Values provided in the assigment
S0: int # current stock price
K: int # strike price of option
r: float # constant risk-free interest rate
sigma: float # constant volatility of the stock price
T: float # time to maturity
N: int # number of time steps

# European Option Prices according to the Black-Scholes solution
# --------------------------------------------------------------
phi = norm.cdf

def call_option(S0, K, r, sigma, T):
    d1 = (np.log(S0/K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T)) # Provided by assignment
    d2 = d1 - sigma*np.sqrt(T) # Provided by assignment
    return S0 * phi(d1) - K * np.exp(-r * T) * phi(d2) # C = this



# Binomial Model
# --------------
def binomial_tree(S0, K, r, sigma, T, N) -> float:
    delta_t = T/N # how long each interval is
    u = np.exp(sigma * np.sqrt(delta_t)) # up movement
    d = 1/u # down movement
    p = (np.exp(r * delta_t) - d) / (u - d) # risk-neutral probability
    discount_factor = np.exp(-r * delta_t) # discount factor so I don't have to write it each time

    table = np.zeros_like(a=np.zeros(shape=(N+1,N+1)))
    for i in range(N, -1, -1):
        for j in range(i, -1, -1):
            ST = S0 * u**j * d**(i-j)
            if i == N:
                table[i][j] = max(ST-K, 0)
            else:
                fu = table[i+1][j+1] # value from the up branch
                fd = table[i+1][j] # value from the down branch
                table[i][j] = (p*fu + (1-p)*fd) * discount_factor # save the value into the table
    #print(table)
    return table[0][0]

if __name__ == "__main__":
    S0 = 10
    K = 10
    r = 0.02
    sigma = 0.25
    T = 0.25
    n = [10, 100, 1000, 10000]

    for i in n:
        print(f'N = {i}: {binomial_tree(S0, K, r, sigma, T, i)}')

    print(f'Black-Scholes = {call_option(S0, K, r, sigma, T)}')