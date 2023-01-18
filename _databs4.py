from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.section.io/engineering-education/react-and-django-rest-framework/'
page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode('utf-8')
soup=BeautifulSoup(html,'html.parser')
print(soup)