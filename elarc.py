import os 

n1 = input("numder1: ")
if not n1.isdigit():
    exit("plz number")
else :
    n1 = int(n1)
#判斷數字1的正確性
chu = input("select your operation : +,-,*,/: ")
chu = chu.strip()
if chu in ["+","-","*","/"]:
   pass
else :
    exit("Wrong input")
#判斷運算符號正確性

n2 = input("numder2: ")
if not n2.isdigit():
    exit("plz number")
else :
    n2 = int(n2)
#判斷數字2的正確性

def art(n1,n2,chu):    #執行運算
    if chu == "*":
        return n1*n2
    elif chu == "+":
        return n1+n2
    elif chu == "-":
        return n1-n2
    elif chu == "/":
        return n1/n2
    else:
        exit("Wrong input") 

#輸出
print(n1, chu, n2,"=",art(n1,n2,chu))
    
os.system("pause")