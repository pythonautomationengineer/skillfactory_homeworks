def main():
    tickets = int(input("Введите количество билетов: "))  # количество билетов

    #  заранее создадим 2 списка чтобы в цикле заполнить их возрастами посетителей, возраста меньше 18 считать не будем
    age_18_24 = []
    age_25_and_more = []

    # до циклов инициализируем переменные-счетчики
    total_18_24 = 0
    total_25_and_more = 0

    for i in range(tickets):
        age_of_1_person = int(input(f'Введите возраст {i + 1} посетителя из {tickets}: '))

        if 17 < age_of_1_person < 25:
            age_18_24.append(age_of_1_person)
            total_18_24 = len(age_18_24) * 990

        elif age_of_1_person >= 25:
            age_25_and_more.append(age_of_1_person)
            total_25_and_more = len(age_25_and_more) * 1390

    if tickets <= 3:
        s_sale = total_18_24 + total_25_and_more  # сложим стоимости обоих возрастных групп
        print(f'Сумма к оплате: {s_sale} ₽')

    else:
        s_sale = int((total_18_24 + total_25_and_more) * 0.9)  # применим скидку и преобразуем float в int
        print(f'Сумма к оплате с учетом скидки: {s_sale} ₽')


if __name__ == '__main__':  # запустим функцию
    main()
