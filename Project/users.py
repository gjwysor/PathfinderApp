# User NBD Model Class
import logging
from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    
