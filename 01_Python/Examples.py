# Fibbonacci Sequence

nterms=int(input("enter n no of terms="))
n0=0
n1=1
count=0
if nterms<=0:
    print("input valid integer")
elif nterms ==1:
    print("total =",n1)
else:
    while count<nterms: 
        # print(n0)
        print(n1)
        nth = n0+n1
        n0=n1
        n1=nth
        count+=1







# multiplication table
# num = 12
# for i in range(0,10):
#     print(num,"*",i,"=",num*i)