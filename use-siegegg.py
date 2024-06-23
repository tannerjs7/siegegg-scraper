import ast

file_path = './competitions/all.txt'

with open(file_path, 'r') as file:
	file_content = file.read()

players = ast.literal_eval(file_content)

sorted_by_kills = sorted(players.items(), key=lambda item: item[1][0], reverse=True)
for counter, player in enumerate(sorted_by_kills):
	if counter == 20: break
	print(player[0] + ' kills: ' + str(player[1][0]))