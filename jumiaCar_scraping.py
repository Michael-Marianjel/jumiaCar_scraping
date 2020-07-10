from bs4 import BeautifulSoup as soup
from datetime import date, timedelta
import requests
import csv
import re
from multiprocessing.dummy import Pool as ThreadPool


# titles = ['Make', 'Model', 'Year', 'Color', 'Mileage', 'Transmission', 'Fuel', 'Price', 'Location', 'Date', 'URL']

# with open('jumiaCar.csv', encoding = 'utf8', mode = 'a', newline = '') as cars:
#   cars_writer = csv.writer(cars, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
#   cars_writer.writerow(titles)

car_urls = []
def check_none(variable):
    if variable==None: return ''
    else: return variable.text.strip()

def get_car(link):
  print(link) 
  car_info = ['', '', '', '', '', '', '', '', '', '', '']
  page_response = requests.get(link)
  page_content = soup(page_response.content, 'html.parser')
  
  car_info[7] = check_none(page_content.find('span', {"class":"price"}))

  try:
    seller_detail = page_content.find('div',{'class':'seller-details'}).findAll('dd')
    car_info[8] = seller_detail[1].text
    car_info[9] = seller_detail[2].text
  except:
    pass
  try:

    for i in range(14):
      if (car_info[9].count("Aujourd'hui") > 0):
        day_month = str(date.today()).split("-")
        car_info[9] = day_month[2] + "/" + day_month[1]
      elif (car_info[9].count("Hier") > 0):
        today = date.today()
        yesterday = today - timedelta(days = 1)
        day_month = str(yesterday).split("-")
        car_info[9] = day_month[2] + "/" + day_month[1]
      elif (car_info[9].count("janv") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/01"
        else:
          car_info[9] = str(day) + "/01"
      elif (car_info[9].count("févr") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/02"
        else:
          car_info[9] = str(day) + "/02"
      elif (car_info[9].count("mars") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/03"
        else:
          car_info[9] = str(day) + "/03"
      elif (car_info[9].count("avri") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/04"
        else:
          car_info[9] = str(day) + "/04"
      elif (car_info[9].count("mai") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/05"
        else:
          car_info[9] = str(day) + "/05"
      elif (car_info[9].count("juin") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/06"
        else:
          car_info[9] = str(day) + "/06"
      elif (car_info[9].count("juil") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/07"
        else:
          car_info[9] = str(day) + "/07"
      elif (car_info[9].count("août") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/08"
        else:
          car_info[9] = str(day) + "/08"
      elif (car_info[9].count("sept") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/09"
        else:
          car_info[9] = str(day) + "/09"
      elif (car_info[9].count("octo") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/10"
        else:
          car_info[9] = str(day) + "/10"
      elif (car_info[9].count("nove") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/11"
        else:
          car_info[9] = str(day) + "/11"
      elif (car_info[9].count("déce") > 0):
        day = int(re.search(r'\d+', car_info[9]).group(0))
        if (day<10):
          car_info[9] = "0" + str(day) + "/12"
        else:
          car_info[9] = str(day) + "/12"

    car_info[10] = page_content.findAll('div', {'class':'slide'})[0].img['data-src']

    if(page_content.find('div',{'class':'new-attr-style'}) != None ):
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

    with open('jumiaCar.csv', encoding = 'utf8', mode = 'a', newline = '') as cars:
      cars_writer = csv.writer(cars, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
      cars_writer.writerow(car_info)
  except:
    pass

def main():
  global car_urls
  nextPage_link = "https://deals.jumia.ci/voitures?page=20408"
  row = 20408
  while(1):
    print(nextPage_link+"                             --------------------"+str(row)+"------------------------")
    page_response = requests.get(nextPage_link)
    page_content = soup(page_response.content, 'html.parser')

    eachCar_links = page_content.findAll("a",{"class":"post-link post-vip"})

    for i in range(len(eachCar_links)):
      car_urls.append("https://deals.jumia.ci/"+eachCar_links[i]['href'])
    if ( len(car_urls) > 500):
      print(len(car_urls))

      pool = ThreadPool(len(car_urls))
      pool.map(get_car, car_urls)
      pool.close()
      pool.join()
      car_urls = []
    
    if (page_content.find('li',{'class':'next'}) != None):
      nextPage_link = "https://deals.jumia.ci" + page_content.find('li',{'class':'next'}).a['href']
    else:
      break
    row += 1


main()