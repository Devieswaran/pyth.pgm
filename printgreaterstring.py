a=str(input("Enter the string:" ))
b=str(input("Enter the string:" ))
if(len(a)>len(b)):
  print(a)
elif(len(a)<len(b)):
  print(b)
else:
  print(a or b)


