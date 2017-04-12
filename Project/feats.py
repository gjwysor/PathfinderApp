# Feat NBD Model Class
import logging
from google.appengine.ext import ndb

class Feat(ndb.Model):
    feat_name = ndb.StringProperty(required=True)
