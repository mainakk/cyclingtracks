import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *args, **keywords):
        self.response.out.write(*args, **keywords)
    def render_str(self, template, **parameters):
        t = jinja_env.get_template(template)
        return t.render(parameters)
    def render(self, template, **keywords):
        self.write(self.render_str(template, **keywords))

class MainHandler(Handler):
    def get(self):
        self.render('tracks.html')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
