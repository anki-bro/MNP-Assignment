def F(n):
    for i in range(n):
        out=''
        for j in range(2*n-1):
            if ((j<n-i-1) or (j>=n+i)):
                out+='-'
            else:
                if(j<n):
                    out+= chr(65+j-(n-i-1))
                else:
                    out+= chr(65-j+(n+i-1))
        print(out)
    pass
# Tests
F(10)
F(6)