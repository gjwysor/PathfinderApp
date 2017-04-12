# Skill NBD Model Class
import logging
from google.appengine.ext import ndb

class Skill(ndb.Model):
    skill_name = ndb.StringProperty(required=True)
