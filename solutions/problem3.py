p,l,s=input(),[],""
for x in range(len(p)-1):
 if not p[x]-p[x+1] is -1:
  l.append(s)
  s=""
 else:
  s=p[x+1]    
print(sorted(l))  