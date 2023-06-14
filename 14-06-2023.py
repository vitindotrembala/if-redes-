l=["            joão", "           jose", "              jonas", "        jota"]
l2=[]

for p in l:
    l2.append(p.find('j'))
pos= min(l2)

print (pos)