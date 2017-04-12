# User NBD Model Class
import re
import logging
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class User(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
