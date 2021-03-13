import email.utils
import json
import matplotlib.pyplot as plt

with open('pract3/table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('pract3/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

t_range = range(0, 24)
time = [i * 0 for i in t_range]

for j in messages:
    time[j[1][3]] += 1

plt.bar(t_range, [time[i] for i in t_range])
plt.xlabel('Время')
plt.ylabel('Кол-во обращений')
plt.title('По времени суток')
plt.show()
