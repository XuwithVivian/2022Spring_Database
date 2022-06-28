def to_date(string):
	date = str(string).split('-')
	return date[0] + '/' + date[1] + '/' + date[2][0:2]

def get_equation(a, b, String = True):
	if b == '':
		return 'True'
	else:
		return a + ' = ' + add_qmark(b, String)

def add_qmark(n, String = True):
	if String:
		return '\'' + n + '\''
	else:
		return n
