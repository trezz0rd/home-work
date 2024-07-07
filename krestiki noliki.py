def draw_area():
	for i in area:
		print(*i)

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать')
draw_area()
print()
for turn in range(1, 10):
	print(f'Ход: {turn}')
	if turn % 2 == 0:
		turn_char = '0'
		print('Ходят нолики')
	else:
		turn_char = 'X'
		print('Ходят крестики')
	row = int(input('Введите номер строки: ')) - 1
	column = int(input('Введите номер столбца: ')) - 1
	if area[row][column] == '*':
		area[row][column] = turn_char
	else:
		print('Ячейка занята')
		draw_area()
		continue
	draw_area()