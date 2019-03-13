a,b=bin(int(input()))[2:],bin(int(input()))[2:]
f=[1 if a[i]!=b[i] else 0 for i in range(len(a) if len(a)<len(b) else len(b))]
print(sum(f))