"""
Application to upload different paid courses 
"""
import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Add a button to the main screen
        self.button = Button(text='Click me!')
        self.button.bind(on_press=self.on_button_click)
        self.add_widget(self.button)

        # Add a button to the main screen
        self.button2 = Button(text='By the Dev!!')
        self.button2.bind(on_press=self.on_button_click)
        self.add_widget(self.button2)

    def on_button_click(self, instance):
        print("Button was clicked!")

class AboutScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AndroidApplication(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # White background color
        Window.size = (500 , 300)    

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))  # Add the MainScreen to the ScreenManager
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


def main():
    Window.clearcolor = (1, 1, 1, 1)  # White background color
    Window.size = (500 , 300)    
    app = AndroidApplication()
    app.run()

if __name__ == '__main__':
    main()

# def main():
    # return AndroidApplication()
