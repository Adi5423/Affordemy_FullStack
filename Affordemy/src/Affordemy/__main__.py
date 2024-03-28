# __main__.py
import sys
import threading
import pyttsx3
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , FadeTransition , NoTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.animation import Animation

# Speech start
# Initialize the engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        print("Home button clicked!")

    def show_main_preview(self, instance):
        print("Priview button clicked!")

    def show_main_Top_Courses(self, instance):
        print("Top Courses button clicked!")

    def show_main_Your_Profile(self, instance):
        print("Profile button clicked!")

    def show_main_Paid_For(self, instance):
        print("Paid For button clicked!")

    def show_message(self, instance):
        print("No Such data to Update")

    def show_dev_message(self, instance):
        print("Developed under Aditya and the production of Aistie")

class AboutScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image(source='D://Python//Projects//Full Stack//Textures Logos//Affordemy_Start.png', opacity=0)
        self.add_widget(self.image)

        Clock.schedule_once(self.fade_in, 1)

        def on_touch_down(self, touch):
            self.fade_out(0)
            self.bind(on_touch_down=self.fade_out)
            Clock.schedule_once(self.switch_to_main, 1)

        self.bind(on_touch_down=on_touch_down)

    def fade_in(self, dt):
        fade_in = Animation(opacity=1, duration=3)
        fade_in.start(self.image)

    def fade_out(self, dt, *args):
        if self.image.opacity == 1:
            fade_out = Animation(opacity=0, duration=3)
            fade_out.bind(on_complete=self.unbind_touch_event)
            fade_out.start(self.image)

    def unbind_touch_event(self, *args):
        self.unbind(on_touch_down=self.fade_out)
        
        
    def switch_to_main(self, dt):
        self.manager.current = 'main'

class Affordemy(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (500, 500)

        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

        # Wrap the ScreenManager in FadeTransition
        custom_fade_trans = FadeTransition(duration=1.0)

        def on_current(instance, current_screen, next_screen):
            custom_fade_trans.current = instance.transition.direction
            custom_fade_trans.target = next_screen
            custom_fade_trans.start(instance)

        sm.bind(current=on_current)

        return sm

def main():
    app = Affordemy()
    app.run()

if __name__ == '__main__':
    main()