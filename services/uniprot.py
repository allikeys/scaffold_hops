import urllib.parse
import urllib.request
import pandas

def pdb2uniprot(pdb_ids):
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
    with urllib.request.urlopen(req) as f:
        response = f.readlines()
    for line in response:
        print(line.decode('utf-8').strip().split('\t'))
