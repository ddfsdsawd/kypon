print("                                  СУПЕРМАРКЕТ ")
name = input("ваше ім'я ")
passw = input("Ваш пароль ")
promo = input("Ваш промокод:")
m = 0
if promo =="12AD3":
    print("Ввід промокоду успішний")
    m = 70
else:
    print("Такого промокоду не існує")
    m = 0
print("                         Ваш гаманець")
print("")
print("")
print("")
print("                             КУПОН")
print("                              НА")
print("                             ",m,"%")
print("                             ДЛЯ")
print(f"                           {name}")
print("")
print("")
print("")
print("            В МЕРЕЖІ МАГАЗИНІВ 'Делікат'")
