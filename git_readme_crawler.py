#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'https://github.com/IITGuwahati-AI/Learning-Content-DS-Algo'
url2 = 'https://github.com/IITGuwahati-AI/Learning-Content-DS-Algo/tree/master/Week%200'
url3 = input()
r = http.request('GET', url3)
html = r.data

soup = BeautifulSoup(html,'lxml')
readme = soup.find('div',id='readme')

print("Headings")
for i in readme.find_all('h1'):
	print('\t'+i.text)

print("\nSubHeadings")
for j in readme.find_all('h2'):
	print('\t'+j.text)

print("\nLinks")
for j in readme.find_all('a'):
	print('\t'+j.attrs['href'])
