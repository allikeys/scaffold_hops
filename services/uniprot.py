import urllib.parse
import urllib.request

def pdb2uniprot(pdb_ids):
    """ID exchange for mapping PDB IDs to Uniprot IDs
    Input: pdb_ids (list)
    Output: Returns file object with mappings
    """
    url = 'https://www.uniprot.org/uploadlists/'

    params = {
    'from': 'PDB_ID',
    'to': 'ID',
    'format': 'tab',
    'query': ' '.join(pdb_ids)
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    mapping_file = urllib.request.urlopen(req)
    return mapping_file

def pdb2uniprotAC(pdb_ids):
    """ID exchange for mapping PDB IDs to Uniprot IDs
    Input: pdb_ids (list)
    Output: Returns file object with mappings
    """
    url = 'https://www.uniprot.org/uploadlists/'

    params = {
    'from': 'PDB_ID',
    'to': 'ACC',
    'format': 'tab',
    'query': ' '.join(pdb_ids)
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    mapping_file = urllib.request.urlopen(req)
    return mapping_file

