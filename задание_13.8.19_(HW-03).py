def main():
    tickets = int(input("Введите количество билетов: "))  # количество билетов

    #  заранее создадим 2 списка чтобы в цикле заполнить их возрастами посетителей
    age_18_25 = []
    age_25_and_more = []

    # до циклов инициализируем переменные-счетчики
    total_18_24 = 0
    total_25_and_more = 0

    for i in range(tickets):
        a = int(input("Введите возраст посетителя: "))

        if 17 < a < 25:
            age_18_25.append(a)
            total_18_24 = len(age_18_25) * 990

        elif a >= 25:
            age_25_and_more.append(a)
            total_25_and_more = len(age_25_and_more) * 1390

    if tickets <= 3:
        s_sale = total_18_24 + total_25_and_more
        print(f'Сумма к оплате: {s_sale} ₽')

    else:
        s_sale = int((total_18_24 + total_25_and_more) * 0.9)  # применим скидку и преобразуем float в int
        print(f'Сумма к оплате с учетом скидки: {s_sale} ₽')


if __name__ == '__main__':  # запустим функцию
    main()
