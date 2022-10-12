# # 1
# print("I***like***Python")

# # 2
# s = input('Введите что-то: ')
# sep1 = input()
# sep2 = input()
# sep3 = input()
# print(sep1, sep2, sep3, sep='-')

# # 3
# a = int(input("Введите число"))
# print(f"Число - {a}")
# print(f"На одно число меньше {a-1}")
# print(f"На одно число больше {a+1}")

# # 4
# xx = int(input("Ведите число чтобы получить результат:"))
# print(f"{xx} --- {xx*2} --- {xx*3} --- {xx*4} --- {xx*5}")

# # 5
# arrayy = [12, 85, 505, 7, 16]
# for i in arrayy:
#     if i % 2 == 0:
#         print(i)


# # 6
# def evenNums(a):
#     for i in a:
#         if i % 2 == 0:
#             print(i)

# evenNums([33, 20, 884, 13, 18, 0.2])

# # 7
# x = input("Введите 4 цифры: ").split()
# print(max(x))

# Есть список - [1, 2, 3, 4, 5, 6], выведите его в обратном порядке.
arrayy = [1, 2, 3, 4, 5, 6]
arrayy.reverse()
print(arrayy)

# Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, 
# замените его на 200. Обновите список только при первом вхождении числа 20.
list1 = [3, 11, 15, 20, 25]
index = list1.index(20)
list1[index] = 200
print(list1)

# Необходимо удалить пустые строки из списка строк
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)

# Функция to_list() принимает неограниченное количество параметров. 
# Обработайте их так, чтобы на выходе получить список из этих элементов.
def to_list(*args):
    return list(args)
print(to_list(17, 3, 88))
print(to_list('Diana', 'Talantbekova', 'PCS 2-20'))