from django.http import HttpResponse
from django.conf import settings
import re


class BasicAuthMiddleware(object):

    def unauthed(self):
        response = HttpResponse("""<html><title>Auth required</title><body>
                                <h1>Authorization Required</h1></body></html>""", mimetype="text/html")
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        response.status_code = 401
        return response

    def process_request(self, request):
        if getattr(settings, 'BASICAUTH_ACTIVE'):
            try:
                BASICAUTH_USERNAME = getattr(settings, 'BASICAUTH_USERNAME')
                BASICAUTH_PASSWORD = getattr(settings, 'BASICAUTH_PASSWORD')
            except AttributeError:
                raise AttributeError("You've enabled BasicAuth but did not provide a username and/or a password!")

            whitelist = getattr(settings, 'BASICAUTH_WHITELIST', [])

            if whitelist:
                path = request.path

                if path[-1:] == '/':
                    path = path[:-1]

                # check if there's a language in the request path
                languages = getattr(settings, 'LANGUAGES', [])
                for l in languages:
                    if path.startswith("/%s/" % l[0]):
                        path = path.replace("/%s" % l[0], '', 1)
                        break

                if path in whitelist or path + '/' in whitelist:
                    return

                else:
                    for regex in whitelist:
                        try:
                            if re.match(regex, path):
                                return
                        except:
                            pass

            if not 'HTTP_AUTHORIZATION' in request.META:
                return self.unauthed()

            else:
                authentication = request.META['HTTP_AUTHORIZATION']
                (authmeth, auth) = authentication.split(' ', 1)
                if 'basic' != authmeth.lower():
                    return self.unauthed()
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                if username == BASICAUTH_USERNAME and password == BASICAUTH_PASSWORD:
                    return

                return self.unauthed()


# copied from django 1.7a2: https://github.com/django/django/blob/1.7a2/django/contrib/sites/middleware.py
from django.contrib.sites.models import Site


class CurrentSiteMiddleware(object):
    """
    Middleware that sets `site` attribute to request object.
    """

    def process_request(self, request):
        request.site = Site.objects.get_current()
