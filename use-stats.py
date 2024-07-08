import ast

file_path = './competitions/all.txt'

with open(file_path, 'r') as file:
	file_content = file.read()

players = ast.literal_eval(file_content)

def get_stat(stat_name, stat_index, number_of_players):
	print('Top ' + str(number_of_players) + ' players by ' + stat_name)
	for counter, player in enumerate(
		sorted(players.items(), key=lambda item: item[1][stat_index], reverse=True)
	):
		if counter == number_of_players: break
		print(player[0] + ' ' + stat_name + ': ' + str(player[1][stat_index]))

def get_kills(number_of_players=10):
	get_stat('kills', 0, number_of_players)

def get_deaths(number_of_players=10):
	get_stat('deaths', 1, number_of_players)

def get_entry_kills(number_of_players=10):
	get_stat('entry kills', 2, number_of_players)

def get_entry_deaths(number_of_players=10):
	get_stat('entry deaths', 3, number_of_players)

def get_maps(number_of_players=10):
	get_stat('maps', 4, number_of_players)

def get_clutches(number_of_players=10):
	get_stat('clutches', 5, number_of_players)

def get_plants(number_of_players=10):
	get_stat('plants', 6, number_of_players)

def get_players(first_letters=''):
	for player in sorted(players.items(), key=lambda item: item[0]):
		if player[0].startswith(first_letters):
			print(player[0])

get_players()