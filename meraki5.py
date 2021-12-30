list1=["one","two","three","four"]

list2=[1,2,3,4]
d={}
for i in list1:
    for j in list2:
        d[list1[i]]=list2[j]
        list2.remove(j)
print(d)