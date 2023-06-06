def luhn(card_number: str) -> bool:
    """
    Проверка валидности номера карты с помощью алгоритма Луна
    Параметры:
    card_number(str) - Номер карты
    Возвращаемые значения:
    (bool) - Является ли номер карты настоящим 
    """
    check = 7
    all_number = list(map(int, card_number))
    all_number = all_number[::-1]
    for i, num in enumerate(all_number):
        if i % 2 == 0:
            tmp = num*2
            if tmp > 9:
                tmp -= 9
            all_number[i] = tmp
    total_sum = sum(all_number)
    rem = total_sum % 10
    check_sum = 10 - rem if rem != 0 else 0
    return check_sum == check
