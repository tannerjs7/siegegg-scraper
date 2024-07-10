import ast
import streamlit as st


def main():

	st.title('Siege Stats')
	c = st.radio('What would you like to see?', ['Stats', 'Players List'])

	if c == 'Stats':
		a = st.radio('Select the stat',
			[
				'Kills', 'Deaths',
				'Opening Kills', 'Opening Deaths',
				'Maps', 'Clutches', 'Plants',
				'K/D Differential', 'Opening K/D Differential'
			]
		)
		b = st.slider('Choose how many players', 5, 50)
	else:
		b = st.text_input('Enter the first however many letters of the player name')

	#Read data from file
	file_path = './competitions/all.txt'
	with open(file_path, 'r') as file:
		file_content = file.read()
	players = ast.literal_eval(file_content)


	def get_stat(stat_name, stat_index, number_of_players):
		st.header('Top ' + str(number_of_players) + ' players by ' + stat_name)
		for counter, player in enumerate(
			sorted(players.items(), key=lambda item: item[1][stat_index], reverse=True)
		):
			if counter == number_of_players: break
			st.text(str(counter + 1) + '. ' + player[0] + ' ' + stat_name + ': ' + str(player[1][stat_index]))


	def get_differential(stat_name, stat_index, number_of_players):
		st.header('Top ' + str(number_of_players) + ' players by ' + stat_name)
		for counter, player in enumerate(
			sorted(players.items(), key=lambda item: item[1][stat_index] - item[1][1 + stat_index], reverse=True)
		):
			if counter == number_of_players: break
			st.text(str(counter + 1) + '. ' + player[0] + ' ' + stat_name + ': '  + str(player[1][stat_index] - player[1][1 + stat_index]))


	def get_kills(number_of_players):
		get_stat('kills', 0, number_of_players)


	def get_deaths(number_of_players):
		get_stat('deaths', 1, number_of_players)


	def get_entry_kills(number_of_players):
		get_stat('entry kills', 2, number_of_players)


	def get_entry_deaths(number_of_players):
		get_stat('entry deaths', 3, number_of_players)


	def get_maps(number_of_players):
		get_stat('maps', 4, number_of_players)


	def get_clutches(number_of_players):
		get_stat('clutches', 5, number_of_players)


	def get_plants(number_of_players):
		get_stat('plants', 6, number_of_players)

	
	def get_kd(number_of_players):
		get_differential('kill/death differential', 0, number_of_players)


	def get_entry_kd(number_of_players):
		get_differential('opening kill/death differential', 2, number_of_players)


	def get_players(first_letters=''):
		for player in sorted(players.items(), key=lambda item: item[0]):
			if player[0].startswith(first_letters):
				st.text(player[0])

	
	if c == 'Stats':
		if a == 'Kills': get_kills(b)
		elif a == 'Deaths': get_deaths(b)
		elif a == 'Opening Kills': get_entry_kills(b)
		elif a == 'Opening Deaths': get_entry_deaths(b)
		elif a == 'Maps': get_maps(b)
		elif a == 'Clutches': get_clutches(b)
		elif a == 'Plants': get_plants(b)
		elif a == 'K/D Differential': get_kd(b)
		elif a == 'Opening K/D Differential': get_entry_kd(b)
	else:
		get_players(b)


if __name__ == '__main__':
	main()