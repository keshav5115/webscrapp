from bs4 import BeautifulSoup
import requests
page=requests.get('https://www.math-only-math.com/representation-of-data.html')
# print(page.content)
soup=BeautifulSoup(page.content,'html.parser')
table=soup.select('table')[0]
td=table.find('tr').find_all('td')
out=[]
for i in td:
    data=[]
    for j in i:
        data+=[j.text]
    out+=[data]
    # print(data)
print(out)

for i,j in zip(out[0],out[1]):
    print(i,j)  

