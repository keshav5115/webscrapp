from urllib.request import urlopen
import re
url='https://www.section.io/engineering-education/react-and-django-rest-framework/'
page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode('utf-8')
st_title=html.find('<title>')+len('<title>')
en_title=html.find('</title>')

#
match_result=re.findall('django',html,re.IGNORECASE)

# geting title of page
print(html[st_title:en_title])

# counting number of django words in the page
print(len(match_result))