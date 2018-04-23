from tts_parser import parser
import subprocess
import argparse

if __name__ == "__main__":
	s = argparse.ArgumentParser(description='parse a given word into separate units.')
	s.add_argument('file', help='yup\'ik string to be parsed')
	args = s.parse_args()

example = args.file
parsed_output = parser(example)
#print(parsed_output)

po = range(len(parsed_output))
for i,k in enumerate(parsed_output):
	po[i] = 'audiofiles/'+k+'.wav'
retcode = subprocess.call(["sox",po[0],po[1],po[2],po[3],po[4],example+".wav"])