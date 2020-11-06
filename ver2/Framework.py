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
            self.ga.best_fitness = np.max(fitness)
            
            fitness   = self.ga.evolve(x, fitness)
            best_idx = np.argmax(fitness)
            print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx])
            
        

        
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--representation'    , type = str     , default = 'real_value')
    parser.add_argument('--crossover_mode'     , type = str     , default = 'whole')
    parser.add_argument('--popuation_size'    , type = int     , default = 100)
    parser.add_argument('--generation'         , type = int     , default = 500)
    parser.add_argument('--dim'                , type = int     , default = 10)
    parser.add_argument('--bound'              , type = int     , default = 32)
    parser.add_argument('--k'              , type = int     , default = 2)
    
    args = parser.parse_args()
    print(args)
    print("-"*100)
    main = Framwork(args)
    main.train()
    
    
    

    

