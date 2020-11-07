import numpy as np


    


class mutation():
    def __init__(self, mode, bound, dim):
        self.mode  = mode
        self.bound = bound
        self.dim   = dim

    def mutate(self, child):
        if(self.mode == "Bit_flip"):
            child = self.Bit_flip(child)
        elif(self.mode == "random_reset"):
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






