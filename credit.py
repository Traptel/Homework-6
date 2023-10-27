suma = int(input("Введіть суму кредиту:"))
term = int(input('Choose the term - 1 or 5 years: '))

if term not in (1, 5):
    print("Неправильний термін. Будь ласка, введіть 1 або 5 років.")
else:
    term_month = term * 12
    term_total = term * 12

    print("Місяць".center(6),
          "Щомісячний платіж".center(17),
          "Відсоток за місяць".center(19),
          "Заборгованість до сплати".center(14),)

    for term_month in range(1, term_month + 1):
        percent = 0.02 if term_month <= 24 else 0.04
        monthly_payment = (suma / term_total) + (suma * percent)
        monthly_interest = suma * percent
        suma -= (suma / term_total)
        term_total -= 1
        print(str(term_month).center(len("Місяць")),
              "{:.2f}".format(monthly_payment).center(len("Щомісячний платіж")),
              "{:.2f}".format(monthly_interest).center(len("Відсоток за місяць")),
              "{:.2f}".format(suma).center(len("Заборгованість до сплати")))
