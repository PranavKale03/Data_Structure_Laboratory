def con_obst():
    global n
    for i in range(n):
        c[i][i]=0.0
        r[i][i]=0
        wt[i][i]=b[i]
        wt[i][i+1]=b[i]+b[i+1]+a[i+1]
        c[i][i+1]=b[i]+b[i+1]+a[i+1]
        r[i][i+1]=i+1
    c[n][n]=0.0
    r[n][n]=0
    wt[n][n]=b[n]
    for i in range(2,n+1):
        for j in range(n-i+1):
            wt[j][j+i]=b[j+i]+a[j+i]+wt[j][j+i-1]
            c[j][j+i]=9999
            for l in range(j+1,j+i+1):
                if(c[j][j+i]>(c[j][l-1]+c[l][j+i])):
                    c[j][j+i]=c[j][l-1]+c[l][j+i]
                    r[j][j+i]=l
            c[j][j+i]+=wt[j][j+i]
    print("\nOptimal BST is : ")
    print("w[0][",n,"] : ",wt[0][n])
    print("c[0][",n,"] : ",c[0][n])
    print("r[0][",n,"] : ",r[0][n],"\n")

def printx(l1,r1):
    if(l1>=r1):
        return
    if(r[l1][r[l1][r1]-1]!=0):
        print("Left child of ", r[l1][r1], " : ", r[l1][r[l1][r1]-1])
    if(r[r[l1][r1]][r1]!=0):
        print("Right child of ", r[l1][r1], " : ", r[r[l1][r1]][r1])
    printx(l1,r[l1][r1]-1)
    printx(r[l1][r1],r1)
    return

n = int(input("Enter the no. of nodes : "))
a = [0]*20
b = [0]*20
wt = [[0]*20 for i in range(20)]
c = [[0]*20 for i in range(20)]
r = [[0]*20 for i in range(20)]
print("\n** PROGRAM FOR OBST **\n")
print("Enter the probability for successful search : ")
for i in range(1,n+1):
    a[i] = float(input("p[%d]: " %i))
print("\n")
print("Enter the probability for unsuccessful search : ")
for i in range(n+1):
    b[i] = float(input("q[%d]: " %i))
con_obst()
printx(0,n)
