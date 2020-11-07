import numpy as np
import pandas as pd
import copy

class GA():
    def __init__(self, args, env):
        self.representation = args.representation
        self.crossover_mode = args.crossover_mode        
        self.popuation_size = args.popuation_size   # default: 100
        self.generation     = args.generation       # default: 500
        self.dim            = args.dim              # default: 10
        self.bound          = args.bound            # default: 32
        self.k              = args.k
        
        self.pop          = None
        self.env          = env
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
        
    def gray(self ,x):
        pass
    def gray_to_dec(self, x):
        pass

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

    def crossover(self, parent):
        if(self.crossover_mode == 'two_point'):
            child = self.two_point(parent)
        elif(self.crossover_mode == 'whole'):
            child = self.whole(parent)
        return child
        
    def two_point(self, parent):
        pass
        
    def whole(self, parent):
        child = []
        for i in range(0, self.popuation_size, 2):
            a, b = np.random.randint(0, self.popuation_size, size = (2))
            
            child.append((parent[a]*0.9 + parent[b]*0.1))
            child.append((parent[a]*0.1 + parent[b]*0.9))
             
        
        return np.array(child)

    def mutate(self, child):  
        if(self.representation == "bit_string"):
            pass
        elif(self.representation == "real_value"):
            child = self.Random_reset(child)
    
        return child

    def Bit_flip(self, child):
        pass
        
    def Random_reset(self, child):
        '''
        child: (popuation size, dim)
        '''  
        for i in range(child.shape[0]):    
            for j in range(child.shape[1]):
                if(np.random.random()<(1/self.dim)):                  
                    child[i][j] = ((np.random.random(1)-0.5)*self.bound*2)[0]
                
        return np.array(child)

    def evolve(self, x, fitness):
        parent = self.select(x, fitness)
        child  = self.crossover(parent)
        child  = self.mutate(child)
        
        self.survivor(child, parent)
        return self.get_fitness(self.pop)

        
        
        
    def survivor(self, child, parent):
        tmp_fitness= self.get_fitness(child).tolist()
        survivor = np.array( child[[tmp_fitness.index(i) for i in tmp_fitness if i <= self.best_fitness]])
        
        df = pd.DataFrame()
        df["tmp_index"]   = [i for i in range(self.popuation_size)]
        df['fitness'] = self.get_fitness(parent)
        df.sort_values(by = ["fitness"])
        survivor = np.concatenate((survivor,parent[df.tmp_index.values]))

        self.pop = survivor[:self.popuation_size]
        
        

        
        