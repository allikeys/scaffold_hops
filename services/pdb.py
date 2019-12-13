from services.utils import fetch_xml

def file(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/describePDB?structureId={pdb_id}'
    response = fetch_xml(request)
    if response['PDBdescription'] == None:
        data = {}
    else:
        data = response['PDBdescription']['PDB']
    return data

def molecule(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/describeMol?structureId={pdb_id}'
    response = fetch_xml(request)
    if 'error' in response['molDescription']['structureId'].keys():
        data = {}
    else:
        data = response['molDescription']['structureId']
    return data

def ligand(het_id):
    request = f'https://www.rcsb.org/pdb/rest/describeHet?chemicalID={het_id}'
    response = fetch_xml(request)
    if response['describeHet']['ligandInfo'] == None:
        data = {}
    else:
        data = response['describeHet']['ligandInfo']['ligand']
    return data

def go_terms(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/goTerms?structureId={pdb_id}'
    response = fetch_xml(request)
    if response['goTerms'] == None:
        data = {}
    else:
        data = response['goTerms']['term']
    return data 

def pfam(pdb_id):
    request = f'https://www.rcsb.org/pdb/rest/hmmer?structureId={pdb_id}'
    response = fetch_xml(request)
    if response['hmmer3'] == None:
        data = {}
    else:
        data = response['hmmer3']['pfamHit']
    return data

