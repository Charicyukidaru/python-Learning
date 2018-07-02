#  multiplication table
import os
for x1 in range(1, 10):
    for x2 in range(1,10):
         x3 = x1 * x2
         print ("%d*%d=%.2d" % (x1, x2 ,x3), end=" ")
    print(" ")
    
os.system("pause")