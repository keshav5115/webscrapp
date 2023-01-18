import requests
from bs4 import BeautifulSoup
import csv

url='https://html.com/'
page=requests.get(url)
soup_page=BeautifulSoup(page.content,'html.parser')
#---------scrapping sidebar content-----------------------

# container=soup_page.find(id='toc_container')
# title=container.find_all('ul',class_='toc_list')
# for i in title:
#     anchor=i.find_all('span')
# container.next_sibling
# result=[]

# for j in anchor:
#     result+=[[j.text,j.next_sibling]]
    




# with open('content.csv','w',newline='') as file:
#     fields=['serial_no','content']
#     data=  csv.writer(file)
#     data.writerow(fields)
#     data.writerows(result)

#-----------scrapping headings of the---------
heading1=soup_page.find_all('h1')
heading2=soup_page.find_all('h2')
heading3=soup_page.find_all('h3')
heading4=soup_page.find_all('h4')
heading5=soup_page.find_all('h5')
heading6=soup_page.find_all('h6')
# for i in heading2:
#     print(i.text)
head_tag=[heading1,heading2,heading3,heading4,heading5,heading6]

def store(file,result=[]):
    for i in file:
        result+=[i.text]
    return result

output=[]

for tag in head_tag:
    output+=[store(tag)]

print(output)
# print(result)
with open('headings.txt','w',newline='') as file1:

    file1.writelines
