def f(a):
    a1=a+1
    for i in range(1,2414141241):
        b=a*i
        b1=a1*i
        s=0
        for i1 in '0123456789':
            if str(b1).count(i1)==str(b).count(i1):
                s+=1
        if s==10:
            return i

print(f(325),"  ",f(100))
