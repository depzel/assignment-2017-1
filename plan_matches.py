input_filename = 'couples_file.txt'

c = []
play() = False

with open(input_filename) as list_input:

	for line in list_input:

		c.append(line) 
		par = [x for x in line.split()]

		for day in range(9):

			if play[par[0]] == False:
				if play[par[1]] == False:
					c.append(day)
					break
				else:
					day = day + 1
					continue
			else:
				day = day + 1
				continue

print(c)
