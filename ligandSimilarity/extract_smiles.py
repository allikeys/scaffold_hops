import sys
import re
import os
import io
from io import open 

def main():

	# Get list of all PDB ligands: SMILES     HET     name
	all_ligands = open('all_smiles.txt', 'r')
	all_ligands_INFO = all_ligands.readlines()

	# Get list of Ligands in scPDB
	ligand_list = open('ligand_list.txt', 'r')
	ligands_HET = ligand_list.readlines()
	for i in range(len(ligands_HET)):
		ligands_HET[i] = ligands_HET[i].rstrip()

	# New List of ligand SMILES
	smiles = []

	for i in range(len(all_ligands_INFO)):
		line = all_ligands_INFO[i]
		split_line = re.split(r'\s+', line)
		if split_line[1] in ligands_HET:
			print(split_line[0] + ',' + split_line[1])


if __name__ == "__main__":
	main()
