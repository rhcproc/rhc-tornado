
from tornado.web import RequestHandler
from tornado.web import authenticated
from urllib.parse import parse_qs
from handlers.base import BaseHandler

import tornado_swirl as swirl

@swirl.restapi('/login')  
class LoginHandler(BaseHandler):
    def get(self):
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 25 :
            self.write('<center>blocked</center>')
            return
        self.render('login.html')

    def post(self):
        recv_data = parse_qs(self.request.body.decode('utf-8'))
        email = recv_data['email'][0].strip()
        password = recv_data['password'][0].strip()
        
        check = True if email == 'admin@admin.com' and password == 'admin' else False
        if check == True : 
            self.set_secure_cookie("user", email)
            self.set_secure_cookie("incorrect", "0")
            self.redirect("/")
        else:
            incorrect = self.get_secure_cookie("incorrect")
            if not incorrect:
                incorrect = 0
            self.set_secure_cookie("incorrect", str(int(incorrect)+1))
            self.write('<center>something wrong with your data \
                                            <a href="/login">Go Back</a></center>')

@swirl.restapi('/logout')
class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")

@swirl.restapi('/signup')
class SignupHandler(RequestHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        recv_data = parse_qs(self.request.body.decode('utf-8'))
        print(recv_data)
