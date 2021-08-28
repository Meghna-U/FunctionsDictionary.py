s=input("Enter a string:")
def most_frequent(st):
    d=dict()
    for i in st:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    from collections import Counter
    Counter('abracadabra').most_common()
    return d;
p=most_frequent(s)
for j in sorted(p,key=p.get,reverse=True):
    print(j,p[j])

        
