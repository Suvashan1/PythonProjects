from datetime import datetime
from pathlib import Path
import json, glob, random
from hoverable import HoverBehavior
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('C:\\Users\\Suvashan\\Desktop\\PythonProjects\\design.kv')

class LoginScreen(Screen):          #Third highest priority
    def sign_up(self):
        self.manager.current = "signup_screen"   #name of SignUpScreen is used when the sign-up button is pressed
                                                 #the sign_up function is called from the button press
    def log_in(self, name, passw):
        with open("C:\\Users\\Suvashan\\Desktop\\PythonProjects\\user.json") as file:
                users = json.load(file)
        if (name in users and users[name]['password'] == passw):
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

    def enlighten(self, feeling):
        feeling = feeling.lower()
        all_files = glob.glob("C:\\Users\\Suvashan\\Desktop\\PythonProjects\\Files\*txt")
        all_files = [Path(filename).stem for filename in all_files]
        if feeling in all_files:
            with open(f"C:\\Users\\Suvashan\\Desktop\\PythonProjects\\Files//{feeling}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.help.text = random.choice(quotes)

class ImageButton(HoverBehavior, Image, ButtonBehavior):
    pass

class RootWidget(ScreenManager):   #Parent creation of the app object        
    pass

class MainApp(App):             #Highest priority in heirachy in Kivy Apps which returns the app 
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

    
