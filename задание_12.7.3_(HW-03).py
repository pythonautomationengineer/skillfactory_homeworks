def main():
    sum_sum = int(input("Введите сумму, которую планируете положить под проценты: "))
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    percent_list = list(per_cent.values()) 
    deposit = [int(percent_list[0] * sum_sum / 100), int(percent_list[1] * sum_sum / 100),
               int(percent_list[2] * sum_sum / 100), int(percent_list[3] * sum_sum / 100)]
    print(f'Размеры депозитов при заданной сумме: {deposit}')

    deposit_max = deposit.index(max(deposit))  # получим индекс максимального значения депозита
    print(f'Максимальная сумма, которую вы можете заработать — {deposit[deposit_max]}')


if __name__ == '__main__':
    main()
