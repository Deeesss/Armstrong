num = int(input("Enter a number: "))
sum = 0
franta = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** franta
    temp //= 10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
