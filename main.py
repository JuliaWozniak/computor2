from process_sides import process_input
import settings

def main():
	settings.init()
	env = settings.env

	while True:
		s = input('>  ')
		if s == 'stop':
			print('Finally')
			break
		if s == 'describe':
			env.print_vars()
		else:	
			process_input(s)

if __name__ == '__main__':
	main()

