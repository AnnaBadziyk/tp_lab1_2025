print("Вітаємо у калькуляторі витрат на подорож!")

distance = float(input("Введіть відстань до пункту призначення (км): "))
fuel_consumption = float(input("Введіть середню витрату пального (л/100км): "))
fuel_price = float(input("Введіть середню ціну пального (грн/л): "))
passengers = int(input("Введіть кількість пасажирів: "))

total_fuel = (distance / 100) * fuel_consumption
total_cost = total_fuel * fuel_price

cost_per_passenger = total_cost / passengers

print(f"Загальна вартість пального: {total_cost:.2f} грн")
print(f"Вартість пального на одного пасажира: {cost_per_passenger:.2f} грн")
