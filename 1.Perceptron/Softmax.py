import numpy as np


#The L vector defines the output scores of our model
def softmax(L):
    expL=np.exp(L)
    return np.divide(expL, sum(expL))

#Another implementation
def softmax2(L):
    expL=np.exp(L)
    expLsum=sum(expL)
    return expL/expLsum