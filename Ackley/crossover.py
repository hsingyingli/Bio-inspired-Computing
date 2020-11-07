import numpy as np



class crossover():
    def __init__(self, mode, pop_size):
        self.mode           = mode
        self.popuation_size = pop_size 
    
    def crossover(self, parent):
        if(self.mode == 'two_point'):
            child = self.two_point(parent)
        elif(self.mode == 'whole'):
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