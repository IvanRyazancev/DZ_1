# Задача №1. Найдите сумму цифр трехзначного числа.

# *Пример:*
# 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

number = int(input("Введите число: "))

sum = 0
for i in str(number):    
    sum += int(i)
print("Сумма цифр введенного числа: ", sum)


# ***
#import re
#number = float(input("Введите число: "))
#
#NewList = list(map(int, re.findall('\d', str(number))))
#print(str(NewList))
#
#sum = 0
#for i in range(len(NewList)):
#    sum += NewList[i]    
#print("Сумма цифр введенного числа: ", sum)