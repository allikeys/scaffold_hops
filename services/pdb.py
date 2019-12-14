import requests
import xmltodict
import json

def fetch_xml(url):
    """Utility to retreive and process xml files from
    the PDB REST API
    """
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else: 
        data = xmltodict.parse(response.content, attr_prefix='')

    return json.loads(json.dumps(data))

def pdbfile(pdb_id):
    """Fetches description of PDB structure file
    """
    request = f'https://www.rcsb.org/pdb/rest/describePDB?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['PDBdescription']['PDB']
    return data

def pdbmolecule(pdb_id):
    """Fetches description of PDB structure
    """
    request = f'https://www.rcsb.org/pdb/rest/describeMol?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['molDescription']['structureId']
    return data

def pdbligand(het_id):
    """Fetches description of PDB ligand
    """
    request = f'https://www.rcsb.org/pdb/rest/describeHet?chemicalID={het_id}'
    response = fetch_xml(request)
    data = response['describeHet']['ligandInfo']['ligand']
    return data

def go_terms(pdb_id):
    """Fetches GO annotations for PDB structure
    """
    request = f'https://www.rcsb.org/pdb/rest/goTerms?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['goTerms']['term']
    return data 

def pfam(pdb_id):
    """Fetches PFAM annotations for PDB strucutre
    """
    request = f'https://www.rcsb.org/pdb/rest/hmmer?structureId={pdb_id}'
    response = fetch_xml(request)
    data = response['hmmer3']['pfamHit']
    return data

