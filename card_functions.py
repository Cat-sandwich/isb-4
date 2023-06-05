import hashlib
import logging
import multiprocessing as mp

from tqdm import tqdm
from typing import Optional


logger = logging.getLogger()
logger.setLevel('INFO')


def check_card_number(hash: str, card_number: str) -> int:
    """
    Проверка на соответствие номера карты хешу
    Параметры:
    hash(str) - Хеш
    card_number(str) - Номер карты
    Возвращаемые значения:
    (int) - Номер карты, если сооветствует хешу
    0 - если не соответствует
    """
    true_hash = hashlib.blake2b(card_number.encode()).hexdigest()
    if hash == true_hash:
        return int(card_number)
    return 0


def enumerate_card_number(hash: str, bins: list, last_four_numbers: str, core_number: int = mp.cpu_count()) \
        -> Optional[int]:
    """
    Подбор номера карты
    Параметры:
    hash(str) - Хеш 
    bins(list) - Набор БИНов карты
    last_four_numbers(str) - Последние 4 цифры 
    core_number(int) - Количество ядер
    Возвращаемые значения:
    Номер карты, если он найден, если нет - None
    """
    args = []
    for i in range(1000000):
        for j in bins:
            args.append((hash, f"{j}{i:06d}{last_four_numbers}"))
    with mp.Pool(processes=core_number) as p:
        for res in p.starmap(check_card_number, tqdm(args, ncols=120)):
            if res:
                p.terminate()
                return res
    return None
