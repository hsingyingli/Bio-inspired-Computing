import numpy as np 
import matplotlib.pyplot as plt 


class Ackley():
    def __init__(self, dim):
        self.dim = dim

        
    def function(self, x):
        return 20+np.exp(1)-20*np.exp(-0.2 * np.sqrt(1/self.dim) * np.sum(np.power(x,2))) - np.exp(np.sum(np.cos(2*np.pi*x))/self.dim)
    
        

if __name__ == "__main__":
    env = Ackley(10)
    data = np.random.randn(100,10)
   
    print(data.shape)
    fitness = []
    for i in data:
        fitness.append(env.function(i))
    print(np.array(fitness).shape)

