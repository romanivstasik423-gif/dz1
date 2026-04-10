#year = 2026
#print("Hello world")
#print(year)
#age = input("How old are you")
#name = input("What is your name")
#print (f"Привіт {name} ваш вік: " + age + "років ")
#year_of_birth = year-int(age)
#print("Рік народження="+ str(year_of_birth))
#age = int(input("Введіть ваш вік: "))
#if age < 18:
    # print("Вхід заборонено!")

# import random
# secret_number = random.randint (1,100)
# print("Я загадав число від 1 до 100. Спробуй вгадати")
# while True:
#     guess = int(input("Введи число: "))
#
#     if guess < secret_number:
#         print("Занадто маленьке!")
#     elif guess > secret_number:
#         print("Занадто велике!")
#     else:
#         print("ти відгадав")
#  break


n = int(input("Введіть число n: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(f"Факторіал "
      f"{n} дорівнює: {factorial}")