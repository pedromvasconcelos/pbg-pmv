from bs4 import BeautifulSoup

import requests



headers = {
    'authority': 'www.worldometers.info',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en,en-US;q=0.9,pt;q=0.8',
    'cookie': 'fsbotchecked=true; _ga=GA1.2.401308785.1582915094; __gads=ID=154a34d09e1a2651:T=1582915094:S=ALNI_Mbhertqd4VZrUNly6GauKXh8oS4kw; _fsuid=ca872719-62f1-4dba-9aed-a02ff54948da; __qca=P0-1648999499-1582915096924; __atssc=google^%^3B18; cookieconsent_status=dismiss; __cfduid=dce21774b664375907a2dcd9d53ab22981585397427; _fs-test=^{^\\^id^\\^:^\\^40ce474c-8069-4cca-bab5-61d128fb9987^\\^,^\\^split^\\^:0.1,^\\^expiry^\\^:1617605999000,^\\^items^\\^:^[^\\^https://a.pub.network/worldometers-info/pubfig.min.js^\\^,^\\^https://a.pub.network/worldometers-info/ab_test/b4768b4a-c3ab-4e33-ba93-5b2ab40ccbb5/pubfig.min.js^\\^^],^\\^selection^\\^:^\\^https://a.pub.network/worldometers-info/ab_test/b4768b4a-c3ab-4e33-ba93-5b2ab40ccbb5/pubfig.min.js^\\^^}; __beaconTrackerID=26xp7wbst; _fsloc=?i=IE^&c=; _gid=GA1.2.151381359.1585927095; __atuvc=38^%^7C10^%^2C0^%^7C11^%^2C2^%^7C12^%^2C46^%^7C13^%^2C18^%^7C14',
}

response = requests.get('https://www.worldometers.info/coronavirus/', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
print('Country Other, Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered, Active Cases, Serious Critical, Tot Cases/1M pop, Deaths/1M pop, Total Tests, Tests/1M pop', end='')

cells = soup.find_all('td')
for cell in cells:
    value = str(cell.contents).strip(' []').replace('\n','').replace("'","")
    if len(value) < 1:
        print('""', end=',')
    elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz<':
        print('\n' + cell.text, end=',')
    else:
        print('"' + value + '"', end=',')
        
        
