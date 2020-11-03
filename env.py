import numpy as np 
import matplotlib.pyplot as plt 


class Ackley():
    def __init__(self, dim):
        self.dim = dim

    def function(self, x):
        return 20+np.exp(1)-20*np.exp(-0.2 * np.sqrt(1/self.dim) * np.sum(np.power(x,2))) - np.exp(np.sum(np.cos(2*np.pi*x))/self.dim)
    
    def get_y(self, x):
        y = np.array([self.function(np.array([x_i])) for x_i in x])
        return y

    def draw(self, x, y):
        plt.plot(x,y)
        plt.show()