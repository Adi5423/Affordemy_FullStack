# __main__.py
import sys
from kivy import *
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import pyttsx3
import threading

# Speech start 
# Initialize the engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    # engine.stop()

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Add a menu bar at the top
        self.menu_bar = BoxLayout(size_hint_y=0.1, orientation='vertical')
        self.home_button = Button(text='Home', size_hint=(None, None), size=(80, 30), on_release=self.show_main_screen)
        self.preview_button = Button(text='Preview', size_hint=(None, None), size=(85, 30), on_release=self.show_main_preview)
        self.top_courses_button = Button(text='Top Courses', size_hint=(None, None), size=(105, 30), on_release=self.show_main_Top_Courses)
        self.profile_button = Button(text='Your Profile', size_hint=(None, None), size=(103, 30), on_release=self.show_main_Your_Profile)
        self.paid_for_button = Button(text='Paid for', size_hint=(None, None), size=(95, 30), on_release=self.show_main_Paid_For)
        self.menu_bar.add_widget(self.home_button)
        self.menu_bar.add_widget(self.preview_button)
        self.menu_bar.add_widget(self.top_courses_button)
        self.menu_bar.add_widget(self.profile_button)
        self.menu_bar.add_widget(self.paid_for_button)
        self.add_widget(self.menu_bar)

        # Add the start button in the center
        self.center_button = Button(text='Start', size_hint=(None, None), size=(150, 50), on_release=self.show_message, background_color=(0.5, 0.5, 1, 1), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.center_button)

        # Add the by dev button at the bottom
        self.bottom_button = Button(text='By Dev!!', size_hint=(None, None), size=(150, 50), on_release=self.show_dev_message, background_color=(1, 0, 0, 1), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.add_widget(self.bottom_button)

    def show_main_screen(self, instance):
        speak("Home button clicked!")
    def show_main_preview(self, instance):
        speak("Priview button clicked!")
    def show_main_Top_Courses(self, instance):
        speak("Top Courses button clicked!")
    def show_main_Your_Profile(self, instance):
        speak("Profile button clicked!")
    def show_main_Paid_For(self, instance):
        speak("Paid For button clicked!")

    def show_message(self, instance):
        speak("No Such data to Update")

    def show_dev_message(self, instance):
        speak("Developed under Aditya and the production of Aistie")

class AboutScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class Affordemy(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (500, 500)

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(SettingsScreen(name='settings'))

        # Start an event loop that runs in the background
        self.event_loop_thread = threading.Thread(target=self.start_event_loop)
        self.event_loop_thread.start()

        return sm

    def start_event_loop(self):
        clock = Clock.schedule_interval(lambda dt: None, 1.0 / 60.0)
        App.get_running_app().run()
        Clock.unschedule(clock)

    def stop_event_loop(self):
        if self.event_loop_thread is not None and self.event_loop_thread.is_alive():
            self.event_loop_thread.join()
            self.event_loop_thread = None

    def stop(self):
        self.stop_event_loop()
        super().stop()

def main():
    # speak("Welcome Sir!")
    app = Affordemy()
    app.run()

if __name__ == '__main__':
    app = Affordemy()
    app.run()