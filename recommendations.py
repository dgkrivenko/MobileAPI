import pymysql
import config
'''
0 - success
1 - no login
2 - no genre
3 - no films

'''
def get_flight_duration(flight):
	connect = pymysql.connect(host=config.host, 
					      	  user=config.user, 
					      	  passwd=config.passwd, 
					      	  db=config.db)
	cursor = connect.cursor()
	query = "SELECT * from flight WHERE reis_name = '{}'".format(flight)
	cursor.execute(query)
	row = cursor.fetchone()
	result = {}
	if row:
		result['code'] = 0
		result['duration'] = row[5]
		return result
	else:
		result['code'] = 1
		return result

def get_genre_by_login(login):
	connect = pymysql.connect(host=config.host, 
					      	  user=config.user, 
					      	  passwd=config.passwd, 
					      	  db=config.db)
	cursor = connect.cursor()
	query = "SELECT gener from users WHERE login = '{}'".format(login)
	cursor.execute(query)
	row = cursor.fetchone()
	if row:
		return row[0]
	else:
		return 1

def get_genre(genre):
	connect = pymysql.connect(host=config.host, 
					      	  user=config.user, 
					      	  passwd=config.passwd, 
					      	  db=config.db)
	cursor = connect.cursor()
	query = "SELECT * from geners WHERE genre_title = '{}'".format(genre)
	cursor.execute(query)
	row = cursor.fetchone()
	result = {}
	if row:
		result['code'] = 0
		result['gener_id'] = row[1]
		result['genre_name'] = row[2]
		return result
	else:
		result['code'] = 2
		return result

def recomend_by_genre(genre, flight):
	response = {}
	flight_dict = get_flight_duration(flight)
	genre_dict = get_genre(genre)
	if flight_dict['code'] != 0:
		response['code'] = flight_dict['code']
		return response
	if genre_dict['code'] != 0:
		response['code'] = genre_dict['code']
		return response

	duration_flight = flight_dict['duration']
	genre_id = genre_dict['gener_id']
	duration_bottom = 0
	connect = pymysql.connect(host=config.host, 
					      	  user=config.user, 
					      	  passwd=config.passwd, 
					      	  db=config.db)
	cursor = connect.cursor()
	query = "SELECT * from films WHERE geners_id = '{}' AND film_duration BETWEEN {} AND {} ORDER BY rating DESC".format(genre_id, duration_bottom, duration_flight)
	cursor.execute(query)
	rows = cursor.fetchall()
	response = {}
	if rows:
		response['code'] = 0
		response['film_array'] = []
		conunt = 0
		for row in rows:
			print(row)
			response_item = {}
			response_item['film_name'] = row[2]
			response_item['rating'] = str(row[3])
			response_item['duration'] = str(row[4])
			response_item['link'] = row[6]
			response['film_array'].append(response_item)
			conunt += 1
			if conunt == 9:
				break
		return response
	else:
		response['code'] = 3
		return response










