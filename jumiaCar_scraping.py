from bs4 import BeautifulSoup as soup
import requests
import csv
import time
from datetime import date

titles = ['Make', 'Model', 'Year', 'Color', 'Mileage', 'Transmission', 'Fuel', 'Price', 'Location', 'Date', 'URL']

with open('jumiaCar.csv', encoding = 'utf8', mode = 'a', newline = '') as cars:
  cars_writer = csv.writer(cars, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
  cars_writer.writerow(titles)
real_date = ["aujourd'hui", "hier", "janv", "févr", "mars", "avri", "mai", "juin", "juil", "août", "sept", "octo", "nove", "déce"]
def check_none(variable):
    if variable==None: return ''
    else: return variable.text.strip()

def get_car(link):
  car_info = ['', '', '', '', '', '', '', '', '', '', '']
  page_response = requests.get(link)
  page_content = soup(page_response.content, 'html.parser')
  
  car_info[7] = check_none(page_content.find('span', {"class":"price"}))

  seller_detail = page_content.find('div',{'class':'seller-details'}).findAll('dd')
  car_info[8] = seller_detail[1].text
  car_info[9] = seller_detail[2].text
  for i in range(14):
    if (car_info[9].count("aujourd'hui") > 0):
      day_month = str(date.today()).split("-")
      date = day_month[2] + "/" + day_month[1]
      car_info[9] = date
    elif (car_info[9].count("hier") > 0):
  car_info[10] = page_content.findAll('div', {'class':'slide'})[0].img['data-src']

  car_attr = page_content.find('div',{'class':'new-attr-style'}).findAll("h3")
  for i in range(len(car_attr)):
    if (car_attr[i].text.count("Marque") > 0 ):
      car_info[0] = car_attr[i].span.text
    elif (car_attr[i].text.count("Modèle") > 0 ):
      car_info[1] = car_attr[i].span.text
    elif (car_attr[i].text.count("Transmission") > 0 ):
      car_info[5] = car_attr[i].span.text
    elif (car_attr[i].text.count("Carburant") > 0 ):
      car_info[6] = car_attr[i].span.text
    elif (car_attr[i].text.count("Année") > 0 ):
      car_info[2] = car_attr[i].span.text
    elif (car_attr[i].text.count("Kilométrage") > 0 ):
      car_info[4] = car_attr[i].span.text
  print(car_info) 
  with open('jumiaCar.csv', encoding = 'utf8', mode = 'a', newline = '') as cars:
    cars_writer = csv.writer(cars, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    cars_writer.writerow(car_info)

def main():
  nextPage_link = "https://deals.jumia.ci/voitures"
  
  while(1):
    print(nextPage_link)
    time.sleep(2)
    page_response = requests.get(nextPage_link)
    page_content = soup(page_response.content, 'html.parser')

    eachCar_links = page_content.findAll("a",{"class":"post-link post-vip"})

    for i in range(len(eachCar_links)):
      get_car("https://deals.jumia.ci/"+eachCar_links[i]['href'])
    if (page_content.find('li',{'class':'next'}) != None):
      nextPage_link = "https://deals.jumia.ci" + page_content.find('li',{'class':'next'}).a['href']
    else:
      break



main()