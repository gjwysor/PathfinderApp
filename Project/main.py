import logging
import webapp2
import os
import jinja2
import time
from webapp2_extras import sessions

JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)

        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            return self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()


class MainHandler(BaseHandler):
    def get(self):
        #skip login for now
        #template = JINJA_ENVIRONMENT.get_template('Templates/logIn.html')
        template = JINJA_ENVIRONMENT.get_template('Templates/mainHub.html')
        self.response.write(template.render())


class HubHandler(BaseHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Templates/mainHub.html')
        self.response.write(template.render())


class NewWizard(BaseHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Templates/characterWizardBasicInfoONE.html')
        self.response.write(template.render())

config = {
    'webapp2_extras.sessions': {
        'secret_key': 'my-secret-key'
    }
}

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/hub', HubHandler),
    ('/newWizard', NewWizard)
], debug=True, config=config)
