import numpy as np 

array = []
for i in range (5): 
    ele = int(input("Entera num: "))
    array = np.array([ele , *array])
    print(array)

print(array)