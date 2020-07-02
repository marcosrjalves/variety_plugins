from variety.Util import Util
from variety.plugins.IQuoteSource import IQuoteSource
from locale import gettext as _

import logging
import random
import json
import requests

logger = logging.getLogger("variety")

class BibleSource(IQuoteSource):
    @classmethod
    def get_info(cls):
        return {
            "name": "Versículos da Bíblia - PT-BR",
            "description": _("Retorna versículos da bíblia"),
            "author": "Marcos Rodrigo Jung Alves",
            "version": "0.1"
        }

    def supports_search(self):
        return True
    
    def get_quote(self):
        # URL da API da Bíblia
        token = '###'
        # Leia o README para conseguir o token da API
        url = 'https://bibleapi.co/api/verses/nvi/random'

        # Recebe o conteudo da request e "JSONEIA"
        r = requests.get(url, headers = {"Authorization":"Bearer " + token})

        data = r.json()

        # Variável do AUTOR e do TEXTO
        author = data['book']['name'] + ' ' + str(data['chapter']) + ':' + str(data['number'])
        quote = data['text']

        return [{"quote": quote, "author": author }]

    def get_for_author(self):
        return self.get_quote()

    def get_for_keyword(self, keyword):
        return self.get_quote()
    
    def get_random(self):
        return self.get_quote()
