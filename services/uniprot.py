import urllib.parse
import urllib.request
import pandas as pd

def pdb2uniprot(pdb_ids):
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
    df = pd.read_csv(urllib.request.urlopen(req), delimiter='\t') 
    return df
