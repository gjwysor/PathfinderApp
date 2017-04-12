# Party NBD Model Class
import logging
from google.appengine.ext import ndb

class Party(ndb.Model):
    party_name = ndb.StringProperty(required=True)
