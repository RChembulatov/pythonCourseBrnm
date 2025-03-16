import time
from threading import Thread
import requests


# Модуль 6 Уровень 1
def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


start_time = time.time()

thread = [Thread(target=get_thread, args=(
    f"thread_name-{i+1}",)) for i in range(5)]

for t in thread:
    t.start()

for t in thread:
    t.join()

end_time = time.time()
print(f"Уровень 2: Параллельный запуск: {end_time - start_time} сек.")
# 1.0043995380401611 сек.


# Модуль 6 Уровень 2
start_time = time.time()

for i in range(5):
    get_thread(f"thread_name-{i+1}")

end_time = time.time()
print(f"Уровень 2: Последовательный запуск: {end_time - start_time} сек.")
# 5.003901243209839 сек.


# Модуль 6 Уровень 3
def get_html(link):
    response = requests.get(link)
    return response.text


links = [
    "https://www.google.com",
    "https://dzen.ru/",
    "https://mail.ru/",
    "https://www.youtube.com",
    "https://vk.com/",
]

start_time = time.time()

thread = [Thread(target=get_html, args=(i,)) for i in links]

for t in thread:
    t.start()

for t in thread:
    t.join()

end_time = time.time()
print(f"Уровень 3: Параллельный запуск: {end_time - start_time} сек.")
# 0.20344853401184082 сек.

start_time = time.time()
for link in links:
    get_html(link)

end_time = time.time()
print(f"Уровень 3: Последовательный запуск: {end_time - start_time} сек.")
# 0.9089934825897217 сек.
