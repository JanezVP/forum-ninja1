#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler, AboutHandler, LoginHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/login', LoginHandler, name="login-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
], debug=True)
