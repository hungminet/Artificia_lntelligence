#Bai 3: Viết hàm có tham số là một mảng số bất kỳ và sắp xếp mảng tăng dần. Yêu
#cầu: dùng vòng lặp for, dùng list để chứa mảng.
def Xep(array):
    for x in range(len(array)):
        for y in range(len(array)):
            if(array[x]>array[y]):
                array[x], array[y] = array[y], array[x]