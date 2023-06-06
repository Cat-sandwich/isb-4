import logging
import time
import argparse
import json

from card_functions import enumerate_card_number
from files_functions import *
from visualization import create_png_with_statistics
from luhn_algorithm import luhn

logger = logging.getLogger()
logger.setLevel('INFO')

def read_settings(file_with_settings: str = 'settings.json') -> dict:
    """
    Считываем пути из файла
    Параметры:
    file_with_settings(str) -  Путь к файлу 
    Возвращаемые значения:
    settings(dict) - Словарь с путями
    """
    settings = None
    try:
        with open(file_with_settings, 'r') as f:
            settings = json.load(f)
        logging.info("Настройки успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать настройки")
    return settings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-crd', '--card_number', type=int,
                       help='Ищем номер карты с помощью хеша, необходимо указать количество процессов')
    group.add_argument('-sta', '--statistics',
                       help='Получаем статистику, подбирая номер карты на разном количестве процессов')
    group.add_argument('-luhn', '--luhn_algorithm', help='Проверяем корректность номера карты с помощью алгоритма Луна')
    group.add_argument('-vis', '--visualize_statistics', help='Создаем гистограмму по имеющейся статистике')
    args = parser.parse_args()
    settings = read_settings()
   
    if args.card_number:
        card_number = enumerate_card_number(settings['hash'], settings['bin'], 
                                            settings['last_four_numbers'], args.card_number)
        if card_number:
            logging.info(f"Номер карты найден: {card_number}")
            write_data_to_txt_file(str(card_number), settings['card_number'])
        else:
            logging.info("Не удалось найти номер карты")
    elif args.statistics:
        for i in range(1, 21):
            t1 = time.time()
            enumerate_card_number(settings['hash'], settings['bin'], 
                                    settings['last_four_numbers'], i)
            t2 = time.time()
            write_statistics(i, t2 - t1, settings['csv_statistics'])
        logging.info("Статистика успешно посчитана")
    elif args.luhn_algorithm:
        if luhn(read_data_from_txt_file(settings['card_number'])):
            logging.info("Номер карты действителен")
        else:
            logging.info("Номер карты не действителен")
    elif args.visualize_statistics:
        create_png_with_statistics(load_statistics(settings['csv_statistics']), settings['png_statistics'])
        logging.info("Гистограмма успешно создана")
