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
            "name": "Bible Verses - ENG",
            "description": _("Gets verses of the bible"),
            "author": "Marcos Rodrigo Jung Alves",
            "version": "0.1"
        }

    def supports_search(self):
        return True
    
    def get_quote(self):
        url = 'https://labs.bible.org/api/?passage=random&type=json'

        r = requests.get(url)
        data = json.loads(r.text)

        author = data[0]["bookname"] + ' ' + data[0]["chapter"] + ':' + data[0]["verse"]
        quote = data[0]["text"]

        return [{"quote": quote, "author": author }]

    def get_for_author(self):
        return self.get_quote()

    def get_for_keyword(self, keyword):
        return self.get_quote()
    
    def get_random(self):
        return self.get_quote()
