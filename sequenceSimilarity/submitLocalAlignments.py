from io import open
import sys
import subprocess
import pandas as pd


def main(infile):
	input_file = open(infile, 'r')

	first = True
	count = 0
	filename = "seq_" + str(count) + ".fa"
	text_file = open(filename, 'w+')

	line = input_file.readline()
	while (line):
		if (line.startswith('>') and !first):
			outfile = filename.split('.')[0] + ".water"
			subprocess.run(["sbatch", "localAlign.sh", filename, infile, outfile])
			text_file.close()
			break

			count += 1
			filename = "seq_" + str(count) + ".fa"
			text_file = open(filename, 'w+')

		text_file.write(line)
		line = input_file.readline()
		first = False


if __name__ == "__main__":
	try: 
		infile = sys.argv[1]
	except:
		print("Wrong inputs! Required: \n \t Arg 1: Input File.")
		sys.exit()
	main(infile)
