import numpy as np
import pandas as pd
import copy


from mutation  import *
from crossover import *
from env       import *

class Genetic_Algorithm():
    def __init__(self, args):
        self.representation = args.representation      
        self.popuation_size = args.popuation_size   # default: 100
        self.generation     = args.generation       # default: 500
        self.dim            = args.dim              # default: 10
        self.bound          = args.bound            # default: 32
        self.k              = args.k
        
        self.pop          = None
        self.env          = Ackley(args.dim)
        self.crossover    = crossover(args.crossover_mode, args.popuation_size)
        self.mutation     = mutation(args.mutation_mode, args.bound, args.dim)

        self.best_fitness = 9999

    def init_popuation(self):
        if(self.representation == "bit_string"):
            pass
        elif(self.representation == "real_value"):
            # size = (popuation size, dim) , [-bound, bound]
            self.pop  = (np.random.random_sample((self.popuation_size, self.dim)) -0.5) * 2 * self.bound


    def get_fitness(self, x):
        '''
        x      : (popuation size, dim)
        
        return : (popuation size)      fitness of every popuation 
        '''
        fitness = []
        for data in x:
            fitness.append(self.env.function(data))
        return np.array(fitness)
        
    def translateDNA(self):
        if(self.representation == "bit_string"):
            pass
        elif(self.representation == "real_value"):
            return self.pop
        

    def select(self, x, fitness):
        # k-tournament, return (popuation size, dim)
        mate = []
        for i in range(self.popuation_size):
            a = int(np.random.randint(0,self.popuation_size,size = (1)))
            # for j in range(1,self.k):
            b = int(np.random.randint(0,self.popuation_size,size = (1)))
            if(fitness[b] < fitness[a]):
                a = b
            mate.append(x[a])
            

        return np.array(mate)
        
   
    def survivor(self, child, parent):
        tmp_fitness= self.get_fitness(child).tolist()
        survivor = np.array( child[[tmp_fitness.index(i) for i in tmp_fitness if i <= self.best_fitness]])
        
        df = pd.DataFrame()
        df["tmp_index"]   = [i for i in range(self.popuation_size)]
        df['fitness'] = self.get_fitness(parent)
        df.sort_values(by = ["fitness"])
        survivor = np.concatenate((survivor,parent[df.tmp_index.values]))

        self.pop = survivor[:self.popuation_size]
    
    def evolve(self, x, fitness):
        parent = self.select(x, fitness)
        child  = self.crossover.crossover(parent)
        child  = self.mutation.mutate(child)
        
        self.survivor(child, parent)
        return self.get_fitness(self.pop)

    def train(self):
        for generation in range(self.generation):
            x       = self.translateDNA()
            
            fitness = self.get_fitness(x)
            self.best_fitness = np.min(fitness)
            
            fitness   = self.evolve(x, fitness)
            best_idx = np.argmin(fitness)
            
            print('Gen:', generation, '| best fit: %f' % fitness[best_idx])
        
        

        
        