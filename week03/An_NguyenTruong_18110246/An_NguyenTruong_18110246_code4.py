# Tìm hoặc tạo một file dữ liệu tùy ý, định dạng csv. Đọc (dùng pandas) và vẽ dữ liệu trong file đó.

#-------Số lượng chợ có đến 31/12 hàng năm phân theo hạng và phân theo địa phương chia theo Hạng và địa phương và Năm
#-------Đơn vị tính: chợ
#-------Nguồn: Tổng cục thống kê

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\DELL\Downloads\Documents\Nam 2\HK2\Artificial Intelligence\SoLieuSoLuongCho.csv')

List_for_draw = [1,2,3,4,5,9]



for i in List_for_draw:
    x_values = np.arange(2008, 2019)
    temp = data.iloc[i]
    y_values = np.array(temp[1:])
    plt.plot(x_values, y_values)

legends = []
for i in List_for_draw:
    legends.append(data.columns[i])
plt.legend(legends)
plt.title('Số lượng chợ '
          '(Nguồn: Tổng cục thống kê)')
plt.xlabel('Năm')
plt.ylabel('Chợ')

#temp = data.iloc[2]
print(legends)
plt.show()


