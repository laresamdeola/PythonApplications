from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
movies_data = response.text

soup = BeautifulSoup(movies_data, features='lxml')

movie_name = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
greatest_movies = []
greatest_movies_position = []

# Loop through the movie title gotten using beautiful soup, did some manipulation in order to the name and position
for movie in movie_name:
    movie_name = ' '.join(movie.get_text().split()[1:])
    movie_position = int(movie.get_text().split()[0][:-1])
    greatest_movies.append(movie_name)
    greatest_movies_position.append(movie_position)

# Create a pandas dataframe to store the titles and positions
movie_data_frame = pd.DataFrame({
    'position': greatest_movies_position,
    'title': greatest_movies
})

movie_sorted_list = movie_data_frame.sort_values('position', ascending=True, ignore_index=True)

# Using the Python Context Manager
with open('movie_list.txt', 'w') as file:
    file.write(str(movie_sorted_list))

# Saving the list to csv
movies_csv = movie_sorted_list.to_csv('movie_list.csv', index=False)





