# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:12:22 2019

@author: Gaurav
"""
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.autograd import Variable


#defining class
class LinearRegressionModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)
    def forward(self, x):
        out = self.linear(x)
        return out


#for undersatnding how a graph looks like when given random values.
'''
np.random.seed(1)
n=50
x=np.random.randn(n)
y=x*np.random.randn(n)
colors=np.random.randn(n)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y,1))(np.unique(x)))

plt.scatter(x,y,c=colors,alpha=0.5)
plt.show()
'''
#defining variables in numpy
x_values=[i for i in range(11)]
x_train=np.array(x_values,dtype=np.float32)
x_train.shape

x_train=x_train.reshape(-1,1)
x_train.shape
 
print(x_values)
#y_values=[2*i + i for i in x_values]
y_values=[]
for i in x_values:
    result = 2*i + 1
    y_values.append(result)
y_train= np.array(y_values, dtype=np.float32)
y_train.shape

y_train = y_train.reshape(-1,1)
y_train.shape
print(y_values)


#For plotting a graph between the two variables
'''
colors=np.random.randn(11)
plt.plot(np.unique(x_values), np.poly1d(np.polyfit(x_values,y_values,1))(np.unique(x_values)))

plt.scatter(x_values,y_values,c=colors)
plt.show()
'''

input_dim = 1
output_dim = 1

model = LinearRegressionModel(input_dim,output_dim)
criterion = nn.MSELoss()
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
epochs = 100

for epoch in range(epochs):
    epoch +=1
    #converting numpyarray totorch variable
    #y=2x+1
    inputs = Variable(torch.from_numpy(x_train))
    labels = Variable(torch.from_numpy(y_train))
    #clear Gradients w.r.t. parameters
    optimizer.zero_grad()
    
    outputs = model(inputs)
    #calculate loss
    loss = criterion(outputs,labels)
    #getting gradients w.r.t. parameters
    loss.backward()
    #Updating parameters
    optimizer.step()
    
    print('epoch{} , loss{} '.format(epoch , loss.data))

plt.clf()
#purely interference   
predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()
#plot true data
plt.plot(x_train,y_train,'go',label='True data',alpha=0.5)
#plot predicitions
plt.plot(x_train,predicted,'--',label='Predictions',alpha=0.5)

plt.legend(loc='best')
plt.show