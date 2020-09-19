from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('C:\\Users\\Suvashan\\Desktop\\stm32\\PythonProjects\\Mobile Mood App\\design.kv')

class LoginScreen(Screen):          #Third highest priority
    def sign_up(self):
        print("Hey friend")  

class RootWidget(ScreenManager):   #Second highest priority
    pass

class MainApp(App):             #Highest priority in heirachy in Kivy Apps
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

    