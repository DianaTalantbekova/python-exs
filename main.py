# 1
print("I***like***Python")

# 2
s = input('Введите что-то: ')
sep1 = input()
sep2 = input()
sep3 = input()
print(sep1, sep2, sep3, sep=s)

# 3
a = int(input("Введите число"))
print(f"Число - {a}")
print(f"На одно число меньше {a-1}")
print(f"На одно число больше {a+1}")

# 4
xx = int(input("Ведите число чтобы получить результат:"))
print(f"{xx} --- {xx*2} --- {xx*3} --- {xx*4} --- {xx*5}")

# 5
arrayy = [12, 85, 505, 7, 16]
for i in arrayy:
    if i % 2 == 0:
        print(i)


# 6
def evenNums(a):
    for i in a:
        if i % 2 == 0:
            print(i)

evenNums([33, 20, 884, 13, 18, 0.2])

# 7
x = input("Введите 4 цифры: ").split()
print(max(x))