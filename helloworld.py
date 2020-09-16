import sys

def helloworld(num):
	
	for i in range(num):
	    print ('Hello World')

if __name__ == '__main__':
	helloworld(int(sys.argv[1]))


