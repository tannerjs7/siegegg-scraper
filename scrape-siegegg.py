from bs4 import BeautifulSoup
import requests


def main():

  #Convert data from 'X-Y (Z)' format to [X, Y]
  def get_kd(data):
    data = data.split('-')
    return [int(data[0]), int(data[1].split()[0])]


  #Get the nth sibling
  def get_sibling(sib, n):
    for _ in range(n):
      sib = sib.next_sibling
    return sib 


  players = {}
  for num in range(1, 500):

    #Scrape data from SiegeGG
    link = 'https://siege.gg/competitions/' + str(num)
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    table = soup.find('table', attrs={'class':'w-100'})

    #If there are no stats on the SiegeGG page, skip the page
    if table == None: continue
    tr = table.tbody.tr
    
    #Add or update the dictionary with player entries of the following format:
    #'player': [kills, deaths, entry_kills, entry_deaths, maps, clutches, plants]
    while tr != ']':
      player = tr.td.span.a['href'][9:].split('-')[1]
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

      if player not in players:
        players[player] = kd + entry_kd + maps + clutches + plants
      else:
        players[player][0] += kd[0]
        players[player][1] += kd[1]
        players[player][2] += entry_kd[0]
        players[player][3] += entry_kd[1]
        players[player][4] += maps[0]
        players[player][5] += clutches[0]
        players[player][6] += plants[0]
      tr = tr.next_sibling

    #Print the current number to track progress
    print(num)

    # with open('./competitions/' + str(num) + '.txt', 'w') as file:
    #   file.write(str(players))

  #Write the dictionary to the 'competitions/all.txt' file as a string
  with open('./competitions/' + 'all' + '.txt', 'w') as file:
    file.write(str(players))


if __name__ == '__main__':
  main()