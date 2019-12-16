import pandas as pd
import numpy as np
import networkx as nx

from config import pocket_feature_url

pocket_feature_scores = pd.DataFrame()

def get_pocket_scores():
    global pocket_feature_scores

    if pocket_feature_scores.empty:
        # Read in pocket feature similarities and convert to an adjacency matrix
        pf = pd.read_csv(pocket_feature_url, header=None, names=['pocket_0', 'pocket_1', 'weight'])
        pf_matrix = pf.pivot(index='pocket_0', columns='pocket_1', values='weight')

        # Compute cosine similarities from pocket feature score matrix
        diagonal = np.sqrt(np.diag(-1*pf_matrix))
        denominator = np.outer(diagonal, diagonal)
        pocket_feature_scores = (-1*pf_matrix)/denominator

    return pocket_feature_scores


def network(low=0.0, high=1.0):

    scores = get_pocket_scores()
    normalized = scores.copy()

    # Specify desired range
    lower_limit = low
    upper_limit = high

    # Set matrix entries out of specificed range to NaN
    if lower_limit > 0:
        normalized[normalized < lower_limit] = np.nan
    if upper_limit < 1:
        normalized[normalized > upper_limit] = np.nan

    # Set off Diagonal to NaN
    np.fill_diagonal(normalized.values, np.nan)

    # Convert from adjacency matrix to edge list
    normalized_edges = normalized.stack().reset_index()
    normalized_edges = normalized_edges.rename(columns={0:'weight'})

    # Split off ligand IDs from pocket IDs and add them as separate columns
    new = normalized_edges['pocket_0'].str.split("_", expand = True)
    normalized_edges['ligand_0'] = new[1]

    new = normalized_edges['pocket_1'].str.split("_", expand = True)
    normalized_edges['ligand_1'] = new[1]

    # Initialize graph
    PFG = nx.Graph()

    # Iterate through rows of edge list dataframe
    for row in normalized_edges.itertuples():
        
        # If both ligand are the same, do nothing
        ligand_0 = row.ligand_0
        ligand_1 = row.ligand_1
        if ligand_0 == ligand_1:
            continue
            
        # If ligands are different, we pull out pocket IDs and pf cosine similarity
        pocket_0 = row.pocket_0    
        pocket_1 = row.pocket_1
        weight = row.weight
        
        # If we have not seen this pair of ligand before, we add an edge
        if not PFG.has_edge(ligand_0, ligand_1):
            PFG.add_edge(ligand_0, ligand_1, id=[pocket_0, pocket_1], weight=weight)
            
        # Otherise update the edge weight if pf cosine similarity is greater than previous max
        elif weight > PFG[ligand_0][ligand_1]['weight']:
            PFG[ligand_0][ligand_1]['weight'] = weight

    return PFG