from bs4 import BeautifulSoup
import requests
# import csv


#Convert data from 'X-Y (Z)' format to [X, Y]
def get_kd(data):
  data = data.split('-')
  return [int(data[0]), int(data[1].split()[0])]


#Get the nth sibling
def get_sibling(sib, n):
  for _ in range(n):
    sib = sib.next_sibling
  return sib 


for num in range(1, 2):
  #Scrape data from SiegeGG
  link = 'https://siege.gg/competitions/' + str(num)
  page_to_scrape = requests.get(link)
  soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

  table = soup.find('table', attrs={'class':'w-100'})
  tr = table.tbody.tr
  
  #Create a dictionary with entries of the following format:
  #'PLAYER': [KILLS, DEATHS, ENTRY_KILLS, ENTRY_DEATHS, MAPS, CLUTCHES, PLANTS]
  players = {}
  while tr != ']':
    player = tr.td.span.a['href'][9:]
    data = get_sibling(tr.td, 2)
    kd = get_kd(data.text)

    data = get_sibling(data, 1)
    entry_kd = get_kd(data.text)

    data = get_sibling(data, 1)
    maps = [int(data.text)]

    data = get_sibling(data, 4)
    clutches = [int(data.text)]

    data = get_sibling(data, 1)
    plants = [int(data.text)]

    players[player] = kd + entry_kd + maps + clutches + plants
    tr = tr.next_sibling
  print(players)

  # with open('./competitions/' + str(num) + '.txt', 'w') as file:
  #   file.write(str(players))