import numpy as np 
import matplotlib.pyplot as plt 


class Ackley():
    def __init__(self, dim):
        self.dim = dim
        plt.ion()
    def function(self, x):
        return 20+np.exp(1)-20*np.exp(-0.2 * np.sqrt(1/self.dim) * np.sum(np.power(x,2))) - np.exp(np.sum(np.cos(2*np.pi*x))/self.dim)
    
    def get_y(self, x):
        y = np.array([self.function(np.array([x_i])) for x_i in x])
        return y

    def draw(self, pop, fitness):
        plt.cla()
        x     = np.arange(-32,32,0.1)
        y     = self.get_y(x)
        pop_y = self.get_y(pop)
        plt.plot(x,y)
        plt.scatter(pop ,pop_y , s=10, c='k')
        plt.text(-0.05, -0.05, "Fitness=%.4f" % fitness, fontdict={'size': 20, 'color': 'red'})
        plt.pause(1)



if __name__ == "__main__":
    test = Ackley(dim = 32)
    test.draw() 
        