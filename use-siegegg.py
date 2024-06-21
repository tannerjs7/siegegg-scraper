import ast

file_path = '499.txt'

with open(file_path, 'r') as file:
	file_content = file.read()

players = ast.literal_eval(file_content)
for player in players:
	print(player, players[player])