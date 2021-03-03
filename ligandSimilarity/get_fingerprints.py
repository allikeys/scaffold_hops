import sys
import os
import numpy
import pandas as pd
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from io import open

def main():
        lig = open('ligand_list.txt', 'r')
        ligands = lig.readlines()
        smiles = open('smiles_plus_names.txt', 'r')
        smiles_list = smiles.readlines()


        mols = []
        for i in range(len(smiles_list)):
                smiles_list[i] = smiles_list[i].split(',')
                if smiles_list[i][1] in ligands:
                        smile = smiles_list[i][1].encode('ascii', 'ignore')
                        smile = smile.rstrip()
                        mol = [smile,  Chem.MolFromSmiles(smiles_list[i][0])]
                        mols.append(mol)

        fingerprints = []
        for x in range(len(mols)):
                try:
                        fp = FingerprintMols.FingerprintMol(mols[x][1])
                except:
                        fp = 0
                        print('This one didn\'t work')
                if (fp != 0):
                        fp_list = [mols[x][0], fp]
                        fingerprints.append(fp_list)

        numfps = len(fingerprints)
        fingerprint_comparison_table = numpy.zeros((numfps, numfps), dtype=float)
        labels = []
        for j in range(numfps):
                labels.append(fingerprints[j][0])
                for k in range(numfps):
                        fingerprint_comparison_table[j][k] = DataStructs.FingerprintSimilarity(fingerprints[j][1], fingerprints[k][1])



        df = pd.DataFrame(fingerprint_comparison_table, columns=labels)
        csvMatrix = df.to_csv()
        file = open('ligandComparisonsTest.csv', 'w+')
        file.write(csvMatrix.decode('utf-8'))
        file.close()
        print(csvMatrix)

if __name__ == "__main__":
        main()