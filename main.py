from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

top100 = [movie.getText() for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")]
top100.reverse()

with open("movies.txt", "w") as file:
    for movie in top100:
        file.write(f"{movie}\n")
