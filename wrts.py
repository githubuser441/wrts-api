from user import *
from uitgevers import *
from methoden import *
from boeken import *
import requests

class WRTS(object):
    def __init__(self, gebruikersnaam, wachtwoord):
        if requests.get('http://wrts.nl/user.json', auth=(gebruikersnaam, wachtwoord)).status_code == 200:
            self.gebruikersnaam = gebruikersnaam
            self.wachtwoord = wachtwoord
        else:
            raise Exception("kan niet inloggen")

    def get_user(self):
        return User.convert_raw(self, requests.get('http://wrts.nl/user.json', auth=(self.gebruikersnaam, self.wachtwoord)).json())

    def get_uitgevers(self):
        return [Uitgevers.convert_raw(self, a) for a in requests.get('http://wrts.nl/publishers.json', auth=(self.gebruikersnaam, self.wachtwoord)).json()]

    def get_methoden(self, slug):
        return Methoden.convert_raw(self, requests.get('http://wrts.nl/publisher_methods/'+slug+'.json', auth=(self.gebruikersnaam, self.wachtwoord)).json())

    def get_boeken(self, id):
        return Boeken.convert_raw(self, requests.get('http://wrts.nl/covers/'+str(id)+'.json', auth=(self.gebruikersnaam, self.wachtwoord)).json())

















