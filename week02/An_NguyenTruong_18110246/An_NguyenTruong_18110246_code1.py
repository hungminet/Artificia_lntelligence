from math import sqrt
#bai1: giai phuong trinh bac 2
def work(a, b, c):
    if(a==0):
        return -c/b, -c/b
    else:
        delta = b*b-4*a*c
        if(delta<0):
            return 'Phuong trinh','vo nghiem'
        elif(delta == 0):
            return -b/2*a,-b/2*a
        else:
            return (-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a
			
