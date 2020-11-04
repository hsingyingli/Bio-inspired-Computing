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

    def train(self):
        for generation in range(args.generation):
            x       = self.ga.translateDNA()
            fitness = self.ga.get_fitness(x)

            y       = self.ga.evolve(x, fitness)
            best_idx = np.argmax(fitness)
            print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx], '| best y: %f'%np.mean(y[best_idx]))
            self.ga.env.draw(self.ga.pop, fitness[best_idx])
        plt.ioff()
        plt.show()

        
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutate_rate'    , type = float   , default = None)
    parser.add_argument('--mutate_mode'    , type = str     , default = 'bit_flip')
    parser.add_argument('--cross_mode'     , type = str     , default = 'two_point')
    parser.add_argument('--population'     , type = int     , default = 100)
    parser.add_argument('--generation'     , type = int     , default = 500)
    parser.add_argument('--dim'            , type = int     , default = 32)
    parser.add_argument('--bound'          , type = int     , default = 32)
    
    args = parser.parse_args()
    test = Framwork(args)
    test.train()
    
    
    
    

    

