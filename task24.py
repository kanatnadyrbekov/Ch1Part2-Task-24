# Напишите функцию которая будет определять полигдром ли введенная строка. Если да 2
# то печатать “True”, если нет “False”.

a = str(input("Slovo: "))
b = list(a)
if b == b[::-1]:
    print("True")
else:
    print("False")