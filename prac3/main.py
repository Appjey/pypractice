import email.utils
import json
import random

import matplotlib.pyplot as plt

with open('pract3/table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('pract3/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# список часов
t_range = range(0, 24)
time = [i * 0 for i in t_range]
# список дней
d_range = range(0, 7)
day = [i * 0 for i in d_range]

for j in messages:
    time[j[1][3]] += 1
# график по времени
axs[0, 0].bar(t_range, [time[i] for i in t_range])
axs[0, 0].set_xlabel('Время')
axs[0, 0].set_ylabel('Кол-во обращений')
axs[0, 0].set_title('По времени суток')
axs[0, 0].legend()
plt.show()
