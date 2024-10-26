p = int(input("Enter no.of rows : "))
for i in range(0,p):
    print( " " *(p-i-1), end="")
    for k in range(0,i+1):
        print(" # " , end="")
    print()