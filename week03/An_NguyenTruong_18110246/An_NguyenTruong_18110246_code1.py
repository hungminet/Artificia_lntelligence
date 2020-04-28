#Cho numpy array có các phần tử: [-2 6 3 10], viết lệnh để lấy ra các bộ phần tử: [6 3],
#[6 -2], [3 10].
import numpy as np

a = np.array([-2,6,3,10])


print(a[1:3])
print(a[-3::-1])
print(a[2:])