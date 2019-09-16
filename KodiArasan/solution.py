a1=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5!=0):
        a1.append(str(x))
print (','.join(a1))

