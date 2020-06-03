n, m = list(map(int, input().split()))
c = 1
if n%2 == 1:
    aida = n//2
    flag = 0
    while m > 0:
        if flag == 0:
            print(c, c+aida)
            flag = 1
            m-=1
            aida -= 1
        else:
            print(n-c+1,n-c+1-aida)
            flag = 0
            m-=1
            aida -= 1
            c+=1
else:
    aida = n//2-1
    flag = 0
    while m > 0:
        if flag == 0:
            print(c, c+aida)
            flag = 1
            m-=1
            aida -= 1
        else:
            print(n-c+1,n-c+1-aida)
            flag = 0
            m-=1
            aida -= 1
            c+=1
