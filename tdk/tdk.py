import requests

class new_word:
    def __init__(self, word):
        self.word = word
        self.json = self.all_data()

    # returns word's meanings
    def meaning(self):
        json = self.json
        meanings = []
        for information in json[0]["anlamlarListe"]:
            meanings.append(information["anlam"])
        return meanings

    # returns word's json data
    def all_data(self):
        r = requests.get('http://sozluk.gov.tr/gts', params={"ara":self.word})
        json = r.json()
        if 'error' in json:
            raise Exception(json["error"])
        return json
