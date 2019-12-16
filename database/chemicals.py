import pandas as pd
import numpy as np
import networkx as nx


from config import ligand_url

ligand_scores = pd.DataFrame()

def get_ligand_scores():
    global ligand_scores

    if ligand_scores.empty:
        ligand_scores = pd.read_csv(ligand_url, index_col=0)
    return ligand_scores

def network(low=0.0, high=1.0):
    scores = get_ligand_scores()
    ligand_matrix = scores.copy()


    mask = np.ones(ligand_matrix.shape,dtype='bool')
    il1 = np.tril_indices(len(ligand_matrix), k=-1)
    mask[il1] = False
    ligand_matrix.mask(mask, inplace=True)
    # Specify desired range
    lower_limit = low
    upper_limit = high

    # Set matrix entries out of specificed range to NaN
    if lower_limit > 0:
        ligand_matrix[ligand_matrix < lower_limit] = np.nan
    if upper_limit < 1:
        ligand_matrix[ligand_matrix > upper_limit] = np.nan

    ligand_edges = ligand_matrix.stack().reset_index()
    ligand_edges = ligand_edges.rename(columns={'level_0': 'ligand_0','level_1': 'ligand_1', 0:'weight'})

    LIG = nx.Graph()

    # Iterate through rows of edge list dataframe
    for row in ligand_edges.itertuples():
        
        # If both ligand are the same, do nothing
        ligand_0 = row.ligand_0
        ligand_1 = row.ligand_1
        weight = row.weight

        LIG.add_edge(ligand_0, ligand_1, weight=weight)

    return LIG
