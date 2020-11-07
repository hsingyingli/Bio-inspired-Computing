import numpy as np



class crossover():
    def __init__(self, mode, pop_size, pc):
        self.mode           = mode
        self.popuation_size = pop_size 
        self.pc             = pc


    def crossover(self, parent):
        if(self.mode == 'two_point'):
            child = self.two_point(parent)
        elif(self.mode == 'whole'):
            child = self.whole(parent)
        elif(self.mode == "uniform"):
            child = self.uniform(parent)

        return child

    def two_point(self, parent):
        child = []
        for i in range(0, self.popuation_size, 2):
            father, mother = np.random.randint(0, self.popuation_size, size = (2))
            father, mother = parent[father], parent[mother]

            a ,b = np.sort(np.random.randint(1, len(parent[i])-1,size = (2)))
            
            child1 = np.array(father[:a].tolist()   + mother[a:b].tolist() + father[b:].tolist())
            child2 = np.array(mother[:a].tolist()   + father[a:b].tolist() + mother[b:].tolist())
            
            child.append(child1)
            child.append(child2)
            

        return np.array(child)
        
    def whole(self, parent):
        child = []
        for i in range(0, self.popuation_size, 2):
            a, b = np.random.randint(0, self.popuation_size, size = (2))
            
            child.append((parent[a]*0.9 + parent[b]*0.1))
            child.append((parent[a]*0.1 + parent[b]*0.9))
             
        
        return np.array(child)
    
    def uniform(self, parent):
        child = []
        for i in range(0, self.popuation_size, 2):
            a, b = np.random.randint(0, self.popuation_size, size = (2))
            child1 = parent[a]
            child2 = parent[b]

            for j in range(len(parent[a])):
                if(np.random.random() < self.pc):
                    tmp = child2[j]
                    child2[j] = child1[j]
                    child1[j] = tmp

            child.append(child1)
            child.append(child2)

        return np.array(child)