import numpy as np 
import matplotlib.pyplot as plt 


class environment():
    def __init__(self, dim):
        self.dim = dim
    
    def function(self, x):
        return 20+np.exp(1)-20*np.exp(-0.2 * np.sqrt(1/self.dim) * np.sum(np.power(x,2))) - np.exp(np.sum(np.cos(2*np.pi*x))/self.dim)
    
    def result(self, x):
        y = [self.function(np.array([x_i])) for x_i in x]
        return y

    def draw(self, x, y):
        plt.plot(x,y)
        plt.show()



class Ackley():
    def __init__(self, args):
        
        self.CROSS_MODE    = args.cross_mode
        self.MUTATE_RATE   = args.mutate_rate
        self.MUTATE_MODE   = args.mutate_mode
        self.POP_SIZE      = args.population
        self.N_GENERATIONS = args.generation

    def get_fitness(self, pred):
        pass


    def translateDNA(self, pop):
        pass 


    def select(self, pop, fitness):
        pass 

    def crossover(self, parent, pop):
        if(self.CROSS_MODE == 'two_point'):
            child = self.two_point(parent, pop)
        elif(self.CROSS_MODE == 'whole'):
            child = self.whole(parent, pop)
            
        return child

    def two_point(self, parent, pop):
        pass
    
    def whole(self, parent, pop):
        pass

    def mutate(self, child):

        if(self.MUTATE_MODE == 'bit_flip'):
            child = self.Bit_flip(child)
        elif(self.MUTATE_MODE == 'random'):
            child = self.Random_reset(child)

        return child

    def Bit_flip(self, child):
        for i in range(child.shape[0]):
            if(np.random.randn()<self.MUTATE_RATE):
                '''
                IF I = 2 , Translate 10'1'00101 to 10'0'00101 
                '''
                child[i] = child[i] ^ 1

        return child
    
    def Random_reset(self, child):
        for i in range(child.shape[0]):
            if(np.random.randn()<self.MUTATE_RATE):
                child[i] = np.random.randint(0,2)  # random reset to 0 or 1

        return child




if __name__ == "__main__":
    env = environment(32)
    x = np.arange(-32,32,0.2)
    y = env.result(x)
    env.draw(x, y)

    

