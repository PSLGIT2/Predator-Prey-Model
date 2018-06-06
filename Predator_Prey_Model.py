#Predator-Prey- Simulation
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class PredPrey():
    def __init__(self,x0,t,alpha,beta,gamma,delta):
        self.x0 = x0
        self.t = t
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta

    def getInfo(self):
        print('x0: '+'['+str(self.x0[0])+' '+str(self.x0[1])+']'  
              ' t: '+'['+str(self.t[0])+' '+str(self.t[1])  +']'     
                        + 'Alpha: '+str(self.alpha) 
                        +' Beta: ' + str(self.beta)
                        +' Gamma: '+ str(self.gamma)
                        +' Delta: '+ str(self.delta))
    
    def predpreymodel(self,xvec,t):
        x = xvec[0]
        y = xvec[1]
        
        alpha = self.alpha
        beta = self.beta 
        delta = self.delta 
        gamma = self.gamma
        
        dxdt = alpha * x     - beta  * x * y 
        dydt = delta * x * y - gamma * y 
        
        return [dxdt,dydt]
        
    def solve(self):     
        tvec = np.linspace(self.t[0],self.t[1],self.t[2])
        x0vec = [self.x0[0],self.x0[1]]
        
        sol = odeint(self.predpreymodel,x0vec,tvec)
       
        x = sol[:,0]
        y = sol[:,1]
        
        return [tvec,x,y]
    
    def plot(self,t,x,y):
       
        plt.plot(t,x)
        plt.plot(t,y)
        plt.title('Lotka-Volterra-Model')
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.show()
        
pp = PredPrey([10,50],[0,400,200],0.1,0.02,0.4,0.02)
pp.getInfo()
[t,x,y] = pp.solve()
pp.plot(t,x,y)