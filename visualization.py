import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel('INFO')


def create_png_with_statistics(statistics: dict, file_name: str) -> None:
    """
    Создание гистограммы со статистикой и сохраняие ее в png файл
    Параметры:
    statistics(dict) - Статистика
    file_name(str) - Путь к файлу
    Возвращаемые значения:
    None
    """
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Время')
    plt.xlabel('Процессы')
    plt.title('Статистика')
    x = statistics.keys()
    y = statistics.values()
    plt.bar(x, y, color='yellow', width=0.5)
    plt.savefig(file_name)
