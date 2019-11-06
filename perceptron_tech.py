# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:19:40 2019

@author: Gaurav
"""
def activation(inputsummation):
    return 1/(1+2.71**(-inputsummation))
    #used is sigmoid function
     #ReLu function is max value 1 else o   

if __name__=="__main__":
    #input -x and w values
    x=[100,120,150,180,2000,140]
    w=[0.5,0.6,0.1,0.3,0.4,0.2]
    result=[]
    sum=0
    #multiply -getting our final output
    for i in range (6):
        temp=x[i]*w[i]
        result.append(temp)
    
    #summaton - first half of perceptron
    for i in range (6):
        sum+=result[i]
    
    #matematical function - activation function
    y =activation(sum)
    print(y)