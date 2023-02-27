import requests
from bs4 import BeautifulSoup
import csv
data=requests.get('https://www.imdb.com/chart/top/')
print(data)
soup_page=BeautifulSoup(data.content,'html.parser')
res=soup_page.find_all(class_='titleColumn')
rating=soup_page.find_all(class_='ratingColumn imdbRating')

data=[]
movie=[]
year=[]
ratingdata=[]
for i,j in zip(res,rating):
    movie=[i.find('a').text]
    year=[i.find('span').text]
    ratingdata=[j.find('strong').text]
    data+=[{'movie':movie[0],'year':year[0],'rating':ratingdata[0]}]


with open('imdp.csv','w',newline='') as file:
    fieldnames=['movie','year','rating']
    csvfile=csv.DictWriter(file,fieldnames)
    csvfile.writeheader()
    csvfile.writerows(data)

    
    
    

