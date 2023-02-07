#Prolog
#Author: Bahniman Rajkonwar Das
#Email: bdas6@student.gsu.edu
#Section:34
import math
x=float(input())
y=float(input())
z=float(input())
a=math.pow(x,z)
b=math.pow(x,(math.pow(y,z)))
c=math.fabs(x-y)
d=math.sqrt(math.pow(x,z))
print(f'{a:.2f} {b:.2f} {c:.2f} {d:.2f}')