import requests

# returns word's meanings
def search(word):
    json = search_all_data(word)
    meanings = []
    for information in json[0]["anlamlarListe"]:
        meanings.append(information["anlam"])
    return meanings

# returns word's json data
def search_all_data(word):
    r = requests.get('http://sozluk.gov.tr/gts', params={"ara":word})
    json = r.json()
    if 'error' in json:
        raise Exception(json["error"])
    return r.json()
