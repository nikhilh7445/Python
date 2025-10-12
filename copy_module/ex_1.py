# Simple list shallow copy 

import copy 
a = [1,2,3]
b = copy.copy(a)
b[0] = 100
print(a)
print(b)
