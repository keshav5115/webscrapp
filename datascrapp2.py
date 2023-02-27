import requests
from bs4 import BeautifulSoup
import csv
data=requests.get('https://www.imdb.com/chart/top/')
print(data)
soup_page=BeautifulSoup(data.content,'html.parser')
title=soup_page.find_all(class_='titleColumn')
rating=soup_page.find_all(class_='ratingColumn imdbRating')


ratingdata=[]
for i,j in zip(title,rating):
    movie=i.find('a').text
    year=i.find('span').text
    ratingdata=j.find('strong').text
    data+=[{'movie':movie,'year':year,'rating':ratingdata}]


with open('imdp.csv','w',newline='') as file:
    fieldnames=['movie','year','rating']
    csvfile=csv.DictWriter(file,fieldnames)
    csvfile.writeheader()
    csvfile.writerows(data)

    
    
    

