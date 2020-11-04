import numpy as np

class GA():
    def __init__(self, args, env):
        #  arguments
        self.env = env
        self.CROSS_MODE    = args.cross_mode
        self.MUTATE_RATE   = args.mutate_rate
        self.MUTATE_MODE   = args.mutate_mode
        self.POP_SIZE      = args.population
        self.N_GENERATIONS = args.generation

        #initial populatiom
        self.pop = np.random.randint(low = -args.bound, high = args.bound, size = (100,1))
        self.best_fitness = 0
    def get_fitness(self, x):
        y = self.env.get_y([self.gray_to_dec(i) for i in x])
        
        return np.exp(10/y).reshape(-1)



    def translateDNA(self):
        x = np.array([self.gray(int(i)) for i in self.pop])
       
        return x 

    def gray(self ,x):
        flag = 0
        
        if(x <0):
            _bin_ = bin(x)[3:]
            flag = 1
        else:
            _bin_ = bin(x)[2:]

        result =  _bin_[0]
          
        for i in range(0,len(_bin_)-1):
            result += str(int(_bin_[i]) ^ int(_bin_[i+1]))
        if(flag):
            return '1' + result.zfill(6)
        return result.zfill(7)
    
    def gray_to_dec(self, x):
        flag = 0
        if(x[0] == "1"):
            flag = 1
            x = x[1:]
        
        result = x[0]
        for i in range(1, len(x)):
            if(x[i] == '0'):
                result += result[i-1]
            elif(x[i] == '1'):
                result += str(int(result[i-1]) ^ 1)

        result = int(result, 2)
        return result if flag == 0 else -result


    def select(self, x, fitness):
        # idx = np.random.choice(np.arange(self.POP_SIZE), size=self.POP_SIZE, replace=True,\
        #                              p=fitness / fitness.sum())
        # x= x.reshape(-1,1)
        # return x[idx]
        mate = []
        for i in range(self.POP_SIZE):
            a = int(np.random.randint(0,len(x[i])-1,size = (1)))
            b = int(np.random.randint(0,len(x[i])-1,size = (1)))
            if(fitness[b] > fitness[a]):
                a = b
            mate.append(x[a])
        return np.array(mate)


    def crossover(self, parent):
        if(self.CROSS_MODE == 'two_point'):
            child = self.two_point(parent)
        elif(self.CROSS_MODE == 'whole'):
            child = self.whole(parent)
            
        return child

    def two_point(self, parent):
        child = []
        for i in range(0,self.POP_SIZE,2):
            a ,b = np.sort(np.random.randint(1,len(parent[i])-1,size = (2)))
            
            child1 = parent[i][:a]   + parent[i+1][a:b] + parent[i][b:]
            child2 = parent[i+1][:a] + parent[i][a:b]   + parent[i+1][b:]
            child.append(child1)
            child.append(child2)
            


        return np.array(child)
    
    def whole(self, parent):
        pass

    def mutate(self, child):

        if(self.MUTATE_MODE == 'bit_flip'):
            self.MUTATE_RATE = 1. / self.POP_SIZE
            child = self.Bit_flip(child)
        elif(self.MUTATE_MODE == 'random'):
            child = self.Random_reset(child)

        return child

    def Bit_flip(self, child):
        for i in range(child.shape[0]):
            for j in range(len(child[i])):
                if(np.random.random() < self.MUTATE_RATE):
                    '''
                    IF I = 2 , Translate 10'1'00101 to 10'0'00101 
                    '''
                    s    = list(child[i])
                    s[j] = str(int(child[i][j]) ^ 1)
                    child[i] = "".join(s)
        return child
    
    def Random_reset(self, child):
        for i in range(child.shape[0]):
            if(np.random.randn()<self.MUTATE_RATE):
                child[i] = np.random.randint(0,2)  # random reset to 0 or 1

        return child
    
    def evolve(self, x, fitness):
        parent = self.select(x, fitness)
        child = self.crossover(parent)      
        child = self.mutate(child)
        self.survivor(child)

        self.best_fitness = np.max(fitness)

        return self.env.get_y(self.pop)

    def survivor(self, child):
        tmp_fitness= self.get_fitness(child).tolist()
        survivor = np.array( child[[tmp_fitness.index(i) for i in tmp_fitness if i >= self.best_fitness]])
        survivor = np.array([self.gray_to_dec(i) for i in survivor])
        survivor = np.concatenate((survivor,np.sort(np.abs(self.pop)).reshape(-1)))
        
        self.pop = survivor[:100]
        

        
        