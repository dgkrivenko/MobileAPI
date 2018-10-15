import lxml
from lxml import etree
import pandas as pd
f = open('ivi_data.xml')
xml = f.read()
xml = xml.encode()
root = etree.parse('ivi_data.xml')
elem = root.findall(".//content")
data_dict = {}
films_id = []
films_title = []
films_dur = []
ratings = []
geners_id = []
links = []

for node in elem:
	films_id.append(node.findtext('id'))
	films_title.append(node.findtext('title'))
	films_dur.append(node.findtext('duration'))
	kinopoisk_rating = node.findtext('kinopoisk_rating')
	if node.find('posters').find('poster') != None:
		links.append(node.find('posters').find('poster').find('files').find('file').findtext('url'))
	else:
		links.append(None)
	if kinopoisk_rating == None:
		imdb_rating = node.findtext('imdb_rating')
		ratings.append(imdb_rating)
	else:
		ratings.append(kinopoisk_rating)

	geners_id.append(node.find('content_genres').find('content_genre').findtext('content_genre_id'))

data_dict = {
	'film_duration': films_dur,
	'film_title': films_title,
	'film_id': films_id,
	'rating': ratings,
	'geners_id': geners_id,
	'link': links 


}
df = pd.DataFrame(data=data_dict, columns=["film_id", "film_title", "rating", "film_duration", "geners_id", "link"])
df.to_csv('films.csv')
elem_gener = root.findall(".//content_genre")
g_id = []
g_name = []

for node in elem_gener:
	g = node.findtext('id')
	t = node.findtext('title')
	if g != None:
		g_id.append(g)
	if t != None:
		g_name.append(t)

geners_dict = {
	'gener_id': g_id,
	'genre_title': g_name
}

gener_df = pd.DataFrame(data=geners_dict, columns=["gener_id", "genre_title"])
gener_df.to_csv('genre.csv')









