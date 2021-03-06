import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite

import database.pocket_feature as pf
import database.chemicals as chem

from services.uniprot import pdb2uniprot
from services.pdb import pfam


def scaffold_hops(pf_range=[0., 1.], lig_range=[0.,1.]):
    PFG = pf.network(low=pf_range[0], high=pf_range[1])
    LIG = chem.network(low=lig_range[0], high=lig_range[1])
    return scaffold_hop_network(PFG, LIG)
    
def scaffold_hop_network(PFG, LIG):
    SHG = PFG.copy()
    for ligand_0, ligand_1 in PFG.edges:
        try:
            ligand_score = LIG[ligand_0][ligand_1]['weight']
            pf_score = PFG[ligand_0][ligand_1]['weight']

            SHG[ligand_0][ligand_1]['weight'] = pf_score/ligand_score
            SHG[ligand_0][ligand_1]['pf_score'] = pf_score
            SHG[ligand_0][ligand_1]['lig_score'] = ligand_score

        except KeyError:
            SHG.remove_edge(ligand_0, ligand_1)
    return SHG


def projected_graph(Graph):
    nx.set_node_attributes(Graph, bipartite.color(Graph), name='color')

    top = [i for i in Graph.nodes if Graph.nodes[i]['color'] == 1]
    projected = bipartite.overlap_weighted_projected_graph(Graph, top)
    return projected

def get_uniprot_filter(Graph):
    all_pockets = []
    for u,v in Graph.edges:
        pockets = SHG[u][v]['id']
        all_pockets.extend(pockets)
        
    structures, ligands = zip( *[i.split('_') for i in set(all_pockets)] )

    structures = list(set(structures))
    ligands = list(set(ligands))

    pdb_uniprot_mapping = pd.read_csv(pdb2uniprot(structures), sep='\t')
    PUG = nx.from_pandas_edgelist(pdb_uniprot_mapping, source='From', target='To')
    return projected_graph(PUG)

def get_pfam_filter(Graph):

    all_pockets = []
    for u,v in SHG.edges:
        pockets = SHG[u][v]['id']
        all_pockets.extend(pockets)
        
    structures, ligands = zip( *[i.split('_') for i in set(all_pockets)] )

    structures = list(set(structures))

    pdb_pfam_mapping = pfam('')
    pdb_pfam_df = pd.DataFrame(pdb_pfam_mapping).groupby('structureId')
    agg = []
    for i in structures:
        try:
            agg.append( pdb_pfam_df.get_group(i.upper()) )
        except KeyError:
            pass

    pfam_df = pd.concat(agg)
    pfam_df['structureId'] = pfam_df['structureId'].str.lower()
    PfamG = nx.from_pandas_edgelist(pfam_df, source='structureId', target='pfamAcc')
    return projected_graph(PfamG)

def filter_results(SHG, filter_graph):
    filtered = SHG.copy()
    for u,v in filtered.edges:
        try:
            pdb_0, pdb_1 = [i.split('_')[0] for i in filtered[u][v]['id']]
            if filter_graph[pdb_0][pdb_1]['weight'] >= 0.3:
                filtered.remove_edge(u,v)
        except KeyError:
            pass
    return filtered
