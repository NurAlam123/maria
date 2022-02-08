# from bs4 import BeautifulSoup
# import requests
# import os


# url = os.getenv("URL")

# def get_song():
#     html = requests.get(url).text

#     soup = BeautifulSoup(html, "lxml")

#     result_div = soup.find("div", id= "result")
#     song_div = result_div.find_all("div", class_= "name")
#     #print(song_div[0].prettify())
#     songs = []
#     for song in song_div:
#         song_name = song.get_text().replace('Check If Unique?', '').strip().replace('\n\t', '') + " song"
#         songs.append(song_name)
#     return songs