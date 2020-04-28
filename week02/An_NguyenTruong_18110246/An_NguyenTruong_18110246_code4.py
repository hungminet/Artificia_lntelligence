#4: Viết hàm có hai tham số là một mảng số bất kỳ và một tham số boolean tên
#SapXepTang. Nếu tham số SapXepTang có giá trị 0 thì sắp xếp mảng giảm dần, có
#giá trị khác 0 thì sắp tăng dần. Yêu cầu: dùng numpy array để chứa mảng.

import numpy


def Xep(a, SapXepTang):
    if(SapXepTang==0):
        for x in range(a.size):
            for y in range(a.size):
                if(a[x] > a[y]):
                    a[x], a[y] = a[y], a[x]
    else:
        for x in range(a.size):
            for y in range(a.size):
                if(a[x] <= a[y]):
                    a[x], a[y] = a[y], a[x]

