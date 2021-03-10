# Scaffold_hops
## Pipeline Components
* Pocket Similarity 
* Ligand Similarity 
* Sequence Similarity 
* Scaffold Hop Score 
* Supplementary Analysis
      
## Pocket Similarity Calculations
   [Calculation Instructions](https://github.com/allikeys/pocketFEATURE_analysis/)

## Ligand Similarity Calculations
      1. Get list of smiles strings:
            a. Download all smiles strings from the PDB ('all_smiles.txt'), get list of ligand ids of interest ('ligand_list.txt') 
            b. Run 'extract_smiles.py > ligand_smiles.txt'
                  - requires: all_smiles.txt, ligand_list.txt
      
      2. get_fingerprints.py 
            - requires: ligand_smiles.txt, ligand_list.txt
            - output: matrix of ligand similarity scores

## Sequence Similarity Calculations
      Run 'Sequence Similarity.ipynb'
            1. Collect the sequences of protein chains involved in ligand binding and relevant UNIPROT ids. 
      
      Use EMBOSS to computer Smith Waterman local sequence alignments on all sequences. 
            - submitLocalAlignments.py 

## Scaffold Hop Score Calculations
      Scaffold_hop_projection.ipynb
            - Requires: pocket, ligand, and sequence similarity files 
            - Produces: scaffold hop candidates

## Supplementary Analysis
      dataAnalysis.ipynb
            - Requires: pocket, ligand, and sequence similarity matrices
            - Produces: Structural analysis of similarity matrices
    
      
