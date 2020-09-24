from datetime import datetime
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('C:\\Users\\Suvashan\\Documents\\Python\\design.kv')

class LoginScreen(Screen):          #Third highest priority
    def sign_up(self):
        self.manager.current = "signup_screen"   #name of SignUpScreen is used when the sign-up button is pressed
                                                 #the sign_up function is called from the button press
    def log_in(self, name, passw):
        with open("C:\\Users\\Suvashan\\Desktop\\PythonProjects\\user.json") as file:
                users1 = json.load(file)
        if name in users1 and users1[name]['password'] == passw:
            self.manager.current = "signin_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password"



class SignUpScreen(Screen):             #Instance of Screen, used to initialize the sign-up screen
    def add_user(self, name, passw):
        with open("C:\\Users\\Suvashan\\Desktop\\PythonProjects\\user.json") as file:
            users = json.load(file)
        users[name] = {'username': name, 'password': passw,
            'created': datetime.now(). strftime("%Y-%m-%d  %H-%M-%S")}  
        with open("C:\\Users\\Suvashan\\Desktop\\PythonProjects\\user.json", 'w') as file:
            json.dump(users, file)
            self.manager.current = "signup_success"
        
class SignUpSuccess(Screen):
    def user_enter(self):
        self.manager.current = "login_screen"

class SigninSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):   #Parent creation of the app object        
    pass

class MainApp(App):             #Highest priority in heirachy in Kivy Apps which returns the app 
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

    