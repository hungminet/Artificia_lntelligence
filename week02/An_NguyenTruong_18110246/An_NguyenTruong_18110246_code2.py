#bai 2: tinh giai thua
def GiaiThua():
    integer = -1
    while(integer<0):
        integer = int(input('Nhap so nguyen duong: '))
    result = 1
    while(integer>0):
        result = result * integer
        integer = integer - 1
    return  result
