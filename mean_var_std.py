import numpy as np

def calculate(list):
    calculations = {'mean':[],
                    'variance':[],
                    'standard deviation':[],
                    'max':[],
                    'min':[],
                    'sum':[]
                   }
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    calculations['mean']=[[np.mean([list[0],list[3],list[6]]),np.mean([list[1],list[4],list[7]]),np.mean([list[2],list[5],list[8]])],[np.mean([list[0],list[1],list[2]]),np.mean([list[3],list[4],list[5]]),np.mean([list[6],list[7],list[8]])],np.mean(list)] 
  
    calculations['variance']=[[np.var([list[0],list[3],list[6]]),np.var([list[1],list[4],list[7]]),np.var([list[2],list[5],list[8]])],[np.var([list[0],list[1],list[2]]),np.var([list[3],list[4],list[5]]),np.var([list[6],list[7],list[8]])],np.var(list)] 

    calculations['standard deviation']=[[np.std([list[0],list[3],list[6]]),np.std([list[1],list[4],list[7]]),np.std([list[2],list[5],list[8]])],[np.std([list[0],list[1],list[2]]),np.std([list[3],list[4],list[5]]),np.std([list[6],list[7],list[8]])],np.std(list)] 

    calculations['max']=[[np.max([list[0],list[3],list[6]]),np.max([list[1],list[4],list[7]]),np.max([list[2],list[5],list[8]])],[np.max([list[0],list[1],list[2]]),np.max([list[3],list[4],list[5]]),np.max([list[6],list[7],list[8]])],np.max(list)] 

    calculations['min']=[[np.min([list[0],list[3],list[6]]),np.min([list[1],list[4],list[7]]),np.min([list[2],list[5],list[8]])],[np.min([list[0],list[1],list[2]]),np.min([list[3],list[4],list[5]]),np.min([list[6],list[7],list[8]])],np.min(list)] 

    calculations['sum']=[[np.sum([list[0],list[3],list[6]]),np.sum([list[1],list[4],list[7]]),np.sum([list[2],list[5],list[8]])],[np.sum([list[0],list[1],list[2]]),np.sum([list[3],list[4],list[5]]),np.sum([list[6],list[7],list[8]])],np.sum(list)] 
    return calculations