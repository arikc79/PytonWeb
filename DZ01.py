# Python 3
n = int(input("Введіть тризначне число: "))
if not 100 <= abs(n) <= 999:
    print("Помилка: введіть тризначне число")
else:
    n = abs(n)
    d1 = n // 100
    d2 = (n // 10) % 10
    d3 = n % 10
    if d1 < d2 < d3:
        print("зростаюче")
    elif d1 > d2 > d3:
        print("спадаюче")
    else:
        print("різне")


# 2

pas = input("Введіть пароль з 4 цифр: ")
if len(pas) != 4 or not pas.isdigit():
    print("Помилка: пароль має складатися з 4 цифр")
else:
    counts = {}
    for ch in pas:
        counts[ch] = counts.get(ch, 0) + 1
    values = sorted(counts.values())

    # Умови замка:
    # всі цифри однакові — відкрито
    # якщо 2 пари однакових цифр — тривога
    # інакше — нічого не відбувається
    if len(counts) == 1:
        print("відкрито")
    elif len(counts) == 2 and values == [2, 2]:
        print("тривога")
    else:
        print("Все гаразд")

# 3

try:
    profit = int(input("ВВедіть прибуток (ціле число): "))
except ValueError:
    print("Помилка Вводу: потрібно ціле число")
    raise SystemExit(1)

if profit < 0:
    print("Помилка: прибуток не може бути від'ємним")
    raise SystemExit(1)

if profit <= 10_000:
    rate = 0.05
elif profit <= 50_000:
    rate = 0.07
else:
    rate = 0.10

bonus = profit * rate
if profit % 10 == 7:
    bonus *= 2

print(f"процент: {rate*100:.0f}%")
print(f"Бонус: {bonus:.2f}")