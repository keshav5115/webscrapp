import requests
from bs4 import BeautifulSoup
import csv
import re
data=requests.get('https://www.imdb.com/chart/top/')
print(data)
soup_page=BeautifulSoup(data.content,'html.parser')
title=soup_page.find_all(class_='titleColumn')
rating=soup_page.find_all(class_='ratingColumn imdbRating')


data=[]
for i,j in zip(title,rating):
    movie=i.find('a').text
    
    year=i.find('span').text
    rating=j.find('strong').text
    count=j.find('strong')['title']
    user=re.findall('\d+,\d+',count)
   

    data+=[{'movie':movie,'year':year,'rating':rating,'reviewer_count':user[0]}]


with open('imdp.csv','w',newline='') as file:
    fieldnames=['movie','year','rating','reviewer_count']
    csvfile=csv.DictWriter(file,fieldnames)
    csvfile.writeheader()
    csvfile.writerows(data)

    
    
    

