import numpy as np
a = np.array([1, 2, 3, 4])
print(a)
#[1 2 3 4]
type(a)
# numpy.ndarray
a.ndim
# 1
a.size
# 4
arr = np.array([[1, 2, 3], [4, 5, 6]]);
print(arr)
# [[1 2 3]
 # [4 5 6]]
arr.ndim
# 2
arr.size
# 6
arr.shape
# (2, 3)
arr.dtype
# dtype('int32')
ar = np.array([[1, 'a', "world"], [3, 4, 5]])
ar.dtype
# dtype('<U11')
arr
# array([[1, 2, 3],
#        [4, 5, 6]])
