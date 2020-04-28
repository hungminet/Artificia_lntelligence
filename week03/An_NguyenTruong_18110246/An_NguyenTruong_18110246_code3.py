# Sử dụng matplotlib vẽ đồ thị hàm số bậc 2 và bậc 3 tùy ý. Yêu cầu: có trục Ox, Oy,
# grid, legend ghi phương trình của 2 đồ thị, title ghi ‘Đồ thị hàm số’, dùng màu đỏ cho hàm bậc
# 2, màu xanh cho hàm bậc 3.

import matplotlib.pyplot as plt
import numpy as np

x_values = np.arange(-5,5,0.1)
y2_values = x_values**2
y3_values = x_values**3

plt.plot(x_values,y2_values,c='r')
plt.plot(x_values,y3_values,c='b')

plt.grid(True)
plt.title('Do Thi Ham So')
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.legend(['Phuong trinh bac 2: y = x^2','Phuong trinh bac 3: y = x^3'])
plt.show()