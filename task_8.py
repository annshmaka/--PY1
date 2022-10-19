money_capital = 10000
salary = 5000
spend = 6000
# increase = 0.05 по условию
increase = 1.05  # для удобства
month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend:
    money_capital += salary - spend
    spend *= increase
    month += 1
    if money_capital <= spend:
        break
print(month)
