import requests

def get_image(inchikey, image_size=''):
    """Retreives and image of a chemical strucutre given its InchiKey Identifier. Image 
    size can be Small (100x100) or (Large) 300x300

    Input: InchiKey (required), image_size (optional)
    Returns: File object with png image of molecule
    """
    if image_size != '':
        size = f'?image_size={image_size}'
    else:
        size = ''

    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{inchikey}/PNG' + size 
    image = requests.get(url).content
    return image