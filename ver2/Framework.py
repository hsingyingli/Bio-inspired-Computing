import numpy as np 
import matplotlib.pyplot as plt
import argparse 
from env import Ackley
from ga  import GA




class Framwork():
    def __init__(self, args):
        self.args = args
        # environment
        self.env = Ackley(args.dim)

        # genetic algorithms
        self.ga  = GA(args, self.env)
        self.ga.init_popuation()
        
    def train(self):
        for generation in range(self.args.generation):
            x       = self.ga.translateDNA()
            
            fitness = self.ga.get_fitness(x)
            self.ga.best_fitness = np.min(fitness)
            
            fitness   = self.ga.evolve(x, fitness)
            best_idx = np.argmin(fitness)
            
            print('Gen:', generation, '| best fit: %f' % fitness[best_idx])
            
            

        

        
     


    
    

    

