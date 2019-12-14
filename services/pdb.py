from services.utils import fetch_xml

def pdbfile(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/describePDB?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['PDBdescription']['PDB']
    return data

def pdbmolecule(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/describeMol?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['molDescription']['structureId']
    return data

def pdbligand(het_id):
    request = f'https://www.rcsb.org/pdb/rest/describeHet?chemicalID={het_id}'
    response = fetch_xml(request)
    data = response['describeHet']['ligandInfo']['ligand']
    return data

def go_terms(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/goTerms?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['goTerms']['term']
    return data 

def pfam(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/hmmer?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['hmmer3']['pfamHit']
    return data

