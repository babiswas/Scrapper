import requests
from bs4 import BeautifulSoup
import sys

def scrape():
   page=requests.get(sys.argv[1])
   soup=BeautifulSoup(page.txt,'html.parser')
   for link in soup.find_all('a'):
       print(link.get('href'))

if __name__=="__main__":
   scrape()

     