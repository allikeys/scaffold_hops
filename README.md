# Scaffold_hops
Pipeline Components
* Pocket Similarity 
* Ligand Similarity 
* Sequence Similarity 
* Scaffold Hop Score 
* Supplementary Files
      
## Pocket Similarity Calculations
   [Calculation Instructions](https://github.com/allikeys/pocketFEATURE_analysis/)

## Ligand Similarity Calculations
      1. Get list of smiles strings:
            a. Download all smiles strings from the PDB ('all_smiles.txt'), get list of ligand ids of interest ('ligand_list.txt') 
            b. Extract smiles of interest using using extract_smiles.py > ligand_smiles.txt
      2. Get fingerprints using get_fingerprints.py
            - requires ligand_smiles.txt and ligand_list.txt
            - output: matrix of ligand similarity scores

## Sequence Similarity Calculations

    

## Scaffold Hop Score Calculations
    
      
