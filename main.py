import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

URL= "https://timetable.gift.edu.in/"
page= requests.get(URL)

#parse it
soup = BeautifulSoup(page.content, 'html.parser')

links = []

urls = soup.find_all('a')

for link in urls:
    hyper = link.get('href')
    full_url = urljoin(URL, hyper)
    #print(full_url)
    links.append(full_url)

j=5

for i in links[5:]:
    time_table = requests.get(i)
    bsoup = BeautifulSoup(time_table.content, 'html5lib')
    
    filename = f"test_{j}.csv"
    f=open(filename, 'w')
    csv_writer = csv.writer(f)
    
    for tr in bsoup.find_all('tr'):
        data=[]
        
        for th in tr.find_all('th'):
            data.append(th.text)
            
        for td in tr.find_all('td'):
            data.append(td.text)
            
        if data:
            #uncomment this line if you want to print it whole in terminal
            ##print(" {}",format(','.join(data)))
            csv_writer.writerow(data)
            
    f.close()
    j=j+1
