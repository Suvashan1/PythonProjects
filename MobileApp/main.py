from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):          #Third highest priority
    pass    

class RootWidget(ScreenManager):   #Second highest priority
    pass

class MainApp(App):             #Highest priority in heirachy in Kivy Apps
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

<<<<<<< HEAD:main.py
    #folder retry commit__
=======
    #Second commit__
>>>>>>> b98bb37cfa48768ef9a4ab419e1f078ff6908d47:MobileApp/main.py
