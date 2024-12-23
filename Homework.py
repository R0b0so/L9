count = 0
num = int(input("Pick any number"))
while num > 0:
 if num > 0:
  num = num // 10
  count = count + 1
print ("You have ",count, " digits in your number.")