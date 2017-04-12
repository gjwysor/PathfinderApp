# Character NBD Model Class
import logging
from google.appengine.ext import ndb

class Character(ndb.Model):
    char_name = ndb.StringProperty(required=True)
