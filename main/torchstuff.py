import  torch
import numpy as np

data = [[1, 2], [3, 4]]
t = torch.tensor(data)
v = torch.zeros_like(t)
#torch.createTensor = createNewTensor(np.ndarray(weights))
print(t)
print(v)

shape = (2, 3,)
rand_tensor = torch.rand(shape)
print(rand_tensor)
print(rand_tensor.dtype)
if torch.cuda.is_available():
    t = t.to('cuda')
else:
    print(' no cuda :( ')

