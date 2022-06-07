
def operFunc():
	oper = str(input('Выберите операцию: '))
	count = 0	
	if oper == '+':
		N = int(input('Сколько операндов? '))
		for num in range(1, N+1):
			print('Введите операнд', num, end = '')
			a = int(input(': '))
			count += a		
		print('Сумма:', count)
	elif oper == '-':
		N = int(input('Сколько операндов? '))
		for num in range(1, N+1):
			print('Введите операнд', num, end = '')
			a = int(input(': '))
			count -= a		
		print('Сумма:', count)
	elif oper == '*':
		N = int(input('Сколько операндов? '))
		for num in range(1, N+1):
			print('Введите операнд', num, end = '')
			a = int(input(': '))
			count *= a		
		print('Сумма:', count)
	elif oper == '/':
		N = int(input('Сколько операндов? '))
		for num in range(1, N+1):
			print('Введите операнд', num, end = '')
			a = int(input(': '))
			count /= a		
		print('Сумма:', count)
	else:
		print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
		operFunc()


operFunc()
print('Nastena, all is ok')
print('Продвигаемся')