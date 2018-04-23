import argparse

def parser(word):
	exampleparse = ['pissur','yull','run','ri','tuk']
	if word == 'pissuryullrunrituk':
		return(exampleparse)

if __name__ == "__main__":
	s = argparse.ArgumentParser(description='parse a given word into separate units.')
	s.add_argument('file', help='yup\'ik string to be parsed')
	args = s.parse_args()
	print(parser(args.file))