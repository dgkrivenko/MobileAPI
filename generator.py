import random
import pandas as pd


alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
numbers = '0 1 2 3 4 5 6 7 8 9'
numbers = numbers.split()
alphabet = alphabet.split()
port_city_1 = ['Абакан', 'Белгород', 'Братск', 'Брянск', 'Вологда', 'Горно-Алтайск ', 'Ижевск', 'Иркутск', 'Казань', 'Кемерово']
port_city_2 = ['Краснодар', 'Москва', 'Санкт-Петербург', 'Саратов', 'Сочи', 'Сургут', 'Улан-Удэ', 'Ульяновск', 'Чебоксары', 'Якутск']
from_city = []
to_city = []

for i in range(10):
	for j in range(10):
		from_city.append(port_city_1[i])
		to_city.append(port_city_2[j])

reis_arr = []
reis_id = []
time = []

for i in range(100):
	reis = ''
	reis += random.choice(alphabet)
	reis += random.choice(alphabet)
	reis += random.choice(numbers)
	reis += random.choice(numbers)
	reis += random.choice(numbers)
	reis += random.choice(numbers)
	reis_arr.append(reis)
	reis_id.append(i)
	time.append(random.randint(100, 720))

df_dict = {
	'reis_id': reis_id,
	'reis_name': reis_arr,
	'from': from_city,
	'to': to_city,
	'durability': time
}

flight = pd.DataFrame(data=df_dict, columns=["reis_id", "reis_name", 'from', 'to', 'durability'])
flight.to_csv('flight.csv')
