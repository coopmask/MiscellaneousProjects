from bs4 import BeautifulSoup
import requests
import pandas

#get the webpage via the request, and retreive the soup
url = "https://www.imdb.com/list/ls055592025/"
web_page = requests.get(url).text
soup = BeautifulSoup(web_page, 'html.parser')

#maintain the source of the html for the movies that will be accessed
movies = soup.find(class_="lister list detail sub-list").find_all('div', class_="lister-item-content")
all_movies = []

#create a loop to find the specific attributes of the movies from the source
for movie in movies:
    title = movie.find('a', href=True).get_text()
    year = movie.find('span', class_="lister-item-year text-muted unbold").get_text().replace('(', '').replace(')', '')
    runtime = movie.find('span', class_="runtime").get_text()
    genre = movie.find('span', class_="genre").get_text().strip()
    list = [title, year, runtime, genre]
    all_movies.append(list)

#create a csv chart of all of the scraped data
pandas_movie_chart = pandas.DataFrame(all_movies)
pandas_movie_chart.to_csv('movie_chart.csv')

print(pandas_movie_chart)
