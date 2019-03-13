i=input()
a=len(i)
[print(i[:a-x]) for x in range(a)]
[print(i[:x-a]) for x in range(a+2,2*a+1)]