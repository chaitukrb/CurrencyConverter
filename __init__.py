from bs4 import BeautifulSoup
from urllib import request
import urllib
import datetime

def for_date(x):
    if(x<10):
        return '0'+str(x)
    else:
        return str(x)


now = datetime.datetime.now()
p=str(now.year)+'-'+for_date(now.month)+'-'+for_date(now.day)

try:
    url = 'https://xe.com/currencytables/?from=INR&date='+p

    page = request.urlopen(url)

    soup = BeautifulSoup(page,"html.parser")

    table=soup.find('table', class_="tablesorter")

    rows = table.find_all('tr')
except urllib.error.URLError:
    raise ConnectionError
except:
    raise Exception

country_code=[]
country=[]
exchange_rate=[]

for tr in rows:
    cols=tr.findAll('td')
    try:
        country_code.append(cols[0].text.strip())
        country.append(cols[1].text.strip())
        exchange_rate.append(float(cols[3].text.strip()))
    except:
        pass

k=list(map(lambda x,y:(x,y),country,exchange_rate))
data=dict(zip(country_code,k))