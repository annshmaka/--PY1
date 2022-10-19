salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
# increase = 0.03  # рост цен
increase = 1.03  # для удобства
need_money = 0  # количество денег, чтобы прожить 10 месяцев
this_month = 1
# TODO Оформить решение

for this_month in range(months):
   delta = spend - salary
   spend *= 1.03
   need_money += delta
print(round(need_money))
