i="row"
j="column"
for i in range(5):
    for j in range(5):
        if (i==0)or(i==4)or(i+j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#For mirrored Z
i="row"
j="column"
for i in range(5):
    for j in range(5):
        if (i==0)or(i==4)or(i-j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()