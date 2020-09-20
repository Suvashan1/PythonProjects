from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('C:\\Users\\Suvashan\\Documents\\Python\\design.kv')

class LoginScreen(Screen):          #Third highest priority
    def sign_up(self):
        self.manager.current = "signup_screen"   #name of SignUpScreen is used when the sign-up button is pressed
                                                 #the sign_up function is called from the button press


class SignUpScreen(Screen):             #Instance of Screen, used to initialize the sign-up screen
    def add_user(self, name, passw):
        print(name, passw)
        

class RootWidget(ScreenManager):   #Parent creation of the app object        
    pass

class MainApp(App):             #Highest priority in heirachy in Kivy Apps which returns the app 
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

    