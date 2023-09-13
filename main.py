from bs4 import BeautifulSoup
import requests
# import time

def get_uk_ire_data():
    html_text = requests.get('https://promo.betfair.com/betfairsp/prices').text # adding .text means text only, not status code

    soup = BeautifulSoup(html_text,'lxml') # lxml is the parser 
    rows = soup.find_all('tr')

    for row in rows:
        if row.find('a') is not None: #skip first few rows 
            tagname = row.find('a').text.split('.')[0]
            if 'dwbfpricesuk' in tagname or 'dwbfpricesire' in tagname:
                if tagname.endswith('22') or tagname.endswith('23'):
                    a_href = row.find('a')['href']
                    r = requests.get('https://promo.betfair.com'+a_href)
                    filename = a_href.split('/')[3]
                    with open('irishwins.csv','ab') as irewins, open('irishplace.csv','ab') as ireplaces, open('ukwins.csv','ab') as ukwins, open('ukplace.csv','ab') as ukplaces:
                        if 'irewin' in filename:
                            irewins.write(r.content)
                        elif 'ireplace' in filename:
                            ireplaces.write(r.content)
                        elif 'ukwin' in filename:
                            ukwins.write(r.content)
                        elif 'ukplace' in filename:
                            ukplaces.write(r.content)


if __name__ == '__main__':
    # while True:
    get_uk_ire_data()
        # time_wait = 10
        # print(f'Waiting {time_wait} minutes')
        # time.sleep(time_wait*60)





