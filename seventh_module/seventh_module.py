import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


# Модуль 7 Уровень 1
page = requests.get("https://mfd.ru/currency/?currency=USD")
soup = BeautifulSoup(page.text, "html.parser")

currency_table = soup.find("table", {"class": "mfd-table"})
rows = currency_table.find_all("tr")[1:]

dates = []
values = []

date_format = "%d.%m.%Y"

for row in rows:
    row_elements = row.find_all('td')
    date = row_elements[0].text.replace("с ", "")
    currency = row_elements[1]

    if not currency.find("a"):
        currency_value = currency.text
        if currency_value and date:
            dates.append(datetime.strptime(date, date_format))
            values.append(float(currency_value))


# Модуль 7 Уровень 2
plt.figure(figsize=(10, 6))
plt.plot(dates, values)

plt.title('Данные о курсе доллара в разные моменты времени')
plt.xlabel('Дата')
plt.ylabel('Курс доллара')

plt.tight_layout()
ax = plt.gca()

ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
ax.grid()

plt.show()
