import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--string", action="store_true")
group.add_argument("-f", "--file", action="store_true")
parser.add_argument('x',type=str, help="type in the string or the file name")
args = parser.parse_args()
if args.string:
	print(args.x)
elif args.file:
	print(args.x)
	with open(args.x) as file:
		print(file)
else:
    print("Please specify whether --string or --file.")