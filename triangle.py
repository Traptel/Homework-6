n = int(input("Введіть число: "))

for i in range(n):
    number = '1' + '0' * i
    print(f"{i:2} {number.rjust(n)}")
