Number = int(input("Write a number"))
sum = 0
temp = Number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if Number == sum:
    print(Number, "is an Armstrong number")
else:
    print(Number, "is not an Armstrong number")