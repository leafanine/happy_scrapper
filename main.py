import requests
from bs4 import BeautifulSoup
import csv

URL = "https://timetable.gift.edu.in/tt.php?c=1&b=52&sem=4&st=S&s=70"
page = requests.get(URL)

#parsing it
soup = BeautifulSoup(page.content, 'html5lib')
filename = "test.csv"
f=open(filename, 'w')
csv_writer = csv.writer(f)

for tr in soup.find_all('tr'):
  data = []

  for th in tr.find_all('th'):
    data.append(th.text)

  for td in tr.find_all('td'):
    data.append(td.text)

  if data:
    print(" {}".format(','.join(data)))
    csv_writer.writerow(data)

f.close()
