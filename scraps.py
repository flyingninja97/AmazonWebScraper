import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv
import sqlite3

if os.path.exists('g:/Amazon_Scraper'):
	pass
else:
	os.mkdir('g:/Amazon_Scraper')
os.chdir('g:/Amazon_Scraper')
com=[]
stars=[]
f_name=[]
prices=[]
k=1
inp=input('Search Here-->')




def bs_soup(url):

    driver.get(url)
    soup=BeautifulSoup(driver.page_source,'lxml')
    return soup
def search(url):

    bs_soup(url)
    t=driver.find_element_by_id('twotabsearchtextbox')
    t.send_keys(inp)
    submit=driver.find_elements_by_class_name('nav-input')[0]
    submit.click()

def products():
	url=driver.current_url
	global k

	soup=bs_soup(url)
	try:
		for i in range(30):
			x=soup.find('li', {"id": f"result_{k}"})
			k=k+1
			if(x==None):
				break

			f_name.append(x.find('h2')['data-attribute'])
			price = x.find('span',{'class':'a-size-base a-color-price s-price a-text-bold'})

			if (price==None):
				prices.append('NA')
			else:
				prices.append(price.text)

			s=x.find_all('span',{'class':'a-icon-alt'})
			if(len(s)==0):
				stars.append('NA')
			if(len(s)==1):
				if(s[0].text=='prime'):
					stars.append('NA')
				else:
					stars.append(s[0].text)
			if(len(s)==2):
				stars.append(s[1].text)


		
	   		
	   		


			company=x.find_all('span',{'class':'a-size-small a-color-secondary'})
			if(len(company)==0):
				com.append('NA')
			else:

				com.append(company[1].text)
	except Exception as e:
		pass


driver=webdriver.Chrome()
url='http://amazon.in'
search(url)
def clicker():
	
	try:
		driver.execute_script("window.scrollBy(0, -150)") 
		button=driver.find_element_by_id('pagnNextString')
		

		
		button.click()
	except Exception as e:

		
		
		clicker()

		
so=bs_soup(driver.current_url)
max=so.find('span',{'class':'pagnDisabled'}).text


for i in range(int(max)):
	products()
	driver.execute_script("window.scrollTo(0, 4500)")
	clicker()



conn = sqlite3.connect('testfinale.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE E_Commerce
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         COMPANY            CHAR(50)     NOT NULL,
         PRICES        CHAR(50),
         STARS         CHAR(50));''')
print ("Table created successfully")


for i in range(len(f_name)):


	conn.execute("insert into E_Commerce (id,name, company, prices,stars) values (?, ?,?,?,?)",
            (i+1, f_name[i], com[i],prices[i],stars[i]))
conn.commit()
conn.close()



