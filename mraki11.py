d = {'a':50,"b":58,'c':56,'d':40,'e':100,'f':20}
max=0
smax=0
tmax=0
for i in d :
    if d[i]>max :
        max=d[i]
    elif smax<max and smax<d[i]:
        smax=d[i]
    elif tmax<smax and tmax<d[i]:
        tmax=d[i]

print(max,smax,tmax)