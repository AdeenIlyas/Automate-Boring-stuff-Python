def collartz(number):
  if number%2==0:
    return number//2
  else:
    return 3*number+1

try:
  num = int(input("Enter the number:\n"))
  result = collartz(num)
  print(result)

  while result!=1:
    result=collartz(result)
    print(result)

except ValueError:
  print("You must enter an integer")
