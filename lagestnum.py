x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[2])
if(a>b and a>c):
  print(a)
elif(c>a and c>b):
  print(c)
elif(b>a and b>c):
  print(b)
else:
	print("Invalid")
