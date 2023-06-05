# INFO
Взаимодействие с пользователем происходит через терминал на этапе вызова программы (main.py)

Для получения справочной информации нужно ввести: python .\main.py -h

Тогда вы получите следующую справочную информацию: usage: main.py [-h] (-crd | -sta | -moon | -vis) options:
  -h, --help            show this help message and exit
  -crd CARD_NUMBER, --card_number CARD_NUMBER
                        Ищем номер карты с помощью хеша, необходимо указать количество процессов
  -sta STATISTICS, --statistics STATISTICS
                        Получаем статистику, подбирая номер карты на разном количестве процессов
  -moon MOON_ALGORITHM, --moon_algorithm MOON_ALGORITHM
                        Проверяем корректность номера карты с помощью алгоритма Луна
  -vis VISUALIZE_STATISTICS, --visualize_statistics VISUALIZE_STATISTICS
                        Создаем гистограмму по имеющейся статистике

В файле setting.json прописаны все пути до файлов

# FILES_RESULTS
bin_number.txt - БИН номера 
hash.txt -  значение хеша
last_number.txt - последние 4 цифры карты
card_number.txt - итоговое значение номера карты

