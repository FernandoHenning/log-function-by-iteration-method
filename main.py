
import numpy as np

def log_n(x, n):
    d = np.empty([n, n])  
    
    a0 = (1 + x) / 2 
    g0 = np.sqrt(x)

    for k in range(n): 
        for i in range(n):
            if k == 0:
                d[k][i] = a0
                a0 = (a0 + g0) / 2
                g0 = np.sqrt(a0 * g0)
            else: 
                d[k][i] = (d[k - 1, i] - 4 ** (-k) * d[k - 1, i - 1]) / (1 - 4 ** (-k))

    return (x - 1) / d[-1, -1]
    

x_values = np.linspace(1, 20, num=1000) 

log_calculated = log_n(0.41, 5)
log_numpy = np.log(0.41)
print(f"Log calculated = {log_calculated}\nLog from numpy = {log_numpy}")   

