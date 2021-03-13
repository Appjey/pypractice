import email.utils
import json
from enum import Enum

import matplotlib.pyplot as plt

with open('pract3/table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('pract3/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

messages = [(m['subj'].upper(), m['date'][0:3].upper(), email.utils.parsedate(m['date'])) for m in messages]
print(messages[0])
print(messages[4])
print(messages[5])
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# список часов
t_range = range(0, 24)
time = [i * 0 for i in t_range]
# список дней
d_range = range(0, 7)

days = [i * 0 for i in d_range]


class Days(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6


# заполнение списков из списка сообщений
for j in messages:
    time[j[2][3]] += 1
    for k in d_range:
        days[k] += j.count(Days(k).name)

# график по времени
axs[0, 0].bar(t_range, [time[i] for i in t_range])
axs[0, 0].set_xlabel('Время')
axs[0, 0].set_ylabel('Кол-во обращений')
axs[0, 0].set_title('По времени суток')
# график по дням недели
axs[0, 1].bar([name for name in Days.__members__], [days[i] for i in d_range], color='red')
axs[0, 1].set_xlabel('День недели')
axs[0, 1].set_ylabel('Кол-во обращений')
axs[0, 1].set_title('По дням недели')

plt.show()
