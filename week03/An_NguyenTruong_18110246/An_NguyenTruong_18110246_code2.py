# Tạo một 2D numpy array và thử dùng các hàm max(), max(0), max(1) để để thấy sự khác biệt.
import numpy as np

array = np.array([[1,2,3],[0,0,5]])

print(array.max())
print(array.max(0))
print(array.max(1))
print(array)