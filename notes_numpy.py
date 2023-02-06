import numpy as np
xlist = [1,2,3]
x = np.array(xlist)

xlist = xlist**2
# TypeError: can't multiply sequence by non-int of type 'list'
x**2
# array([1, 4, 9])

y_array = np.array([1,2,3])
y_array > 2
# array([False, False, True])

y_array[y_array > 2]
# array([3])


x = [4 , 9 , 6, 3, 1]
x[1]
# 9
import numpy as np
y = np.array(x)
y[1]
# 9

print(y)
# [4 9 6 3 1]
high = y > 5
y[high]
# array([9, 6])

type(y)
# numpy.ndarray
z = np.array([1,2,3],[4,5,6])
type(z)
# numpy.ndarray
#   ok doesnt tell us much
z.shape
# (2, 3)
#   ok, so it is a 2x3 array

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]
np_positions = np.array(positions) 
np_heights = np.array(heights)    
gk_heights = np.array(np_heights[np_positions == 'GK'] )
other_heights = np.array(np_heights[np_positions != 'GK'])
print("Median height of goalkeepers: " + str(np.median(gk_heights)) )
print("Median height of other players: " + str(np.median(other_heights)) )

