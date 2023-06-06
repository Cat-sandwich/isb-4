import logging
import csv

logger = logging.getLogger()
logger.setLevel('INFO')


def read_data_from_txt_file(file_name: str) -> str:
    """
    Cчитываение данных из файла
    Параметры:
    file_name(str): Путь к файлу
    Возвращаемые значения:
    data(str) - Строка с данными из файла
    """
    try:
        with open(file_name, 'r') as f:
            data = f.read()
        logging.info("Данные успешно считаны")
    except OSError as err:
        logging.warning(
            f"{err} Не удалось считать данные")
    return data


def write_data_to_txt_file(data: str, file_name: str) -> None:
    """
    Запись данных в файл
    Параметры:
    data(str) - Данные для записи
    file_name(str) - Путь к файлу
    Возвращаемые значения:
    None
    """
    try:
        with open(file_name, 'w') as f:
            f.write(data)
        logging.info("Данные успешно записаны")
    except OSError as err:
        logging.warning(
            f"{err} Не удалось записать данные")


def load_statistics(file_name: str) -> dict:
    """
    Считывание статистики из файла
    Параметры:
    file_name(str) - Путь к файлу
    Возвращаемые значения:
    result(dict) - Словарь: (количество процессов: время)
    """
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            stats = list(reader)
        logging.info("Статистика успешно считана")
    except OSError as err:
        logging.warning(
            f"{err} Не удалось считать статистику")
    result = dict()
    for i in stats:
        processes, time = i
        result[int(processes)] = float(time)
    return result


def write_statistics(processes: int, time: float, file_name: str) -> None:
    """
    Запись статистики в файл
    Параметры:
    processes(int) - Номер процесса
    time(float) - Время 
    file_name(str) - Путь к файлу
    Возвращаемые значения:
    None
    """
    try:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([processes, time])
        logging.info("Статистика успешно записана")
    except OSError as err:
        logging.warning(
            f"{err} Не удалось записать статистику")
