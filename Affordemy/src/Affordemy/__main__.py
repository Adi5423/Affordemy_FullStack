# __main__.py
import sys
import threading
import pyttsx3
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , FadeTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.textinput import TextInput

# Speech start
# Initialize the engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.background_color = (0.9, 1.0, 0.8, 1)

        self.email_input_box = BoxLayout(size_hint=(None, None), width=200, height=300, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.email_label = Label(text='Email:', font_size=18, bold=True)
        self.email_input = TextInput(multiline=False, font_size=16, size_hint=(None, None), width=150)

        self.password_label = Label(text='Password:', font_size=18, bold=True)
        self.password_input = TextInput(multiline=False, password=True, font_size=16, size_hint=(None, None), width=150)

        self.login_button = Button(text='Log in', font_size=18, bold=True, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.email_input_box.add_widget(self.email_label)
        self.email_input_box.add_widget(self.email_input)
        self.email_input_box.add_widget(self.password_label)
        self.email_input_box.add_widget(self.password_input)
        self.email_input_box.add_widget(self.login_button)

        self.add_widget(self.email_input_box)

        self.login_button.bind(on_release=self.handle_login)

    def handle_login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        if email and password:
            print("Successful!")
            self.manager.get_screen('uiPage1').update_background_color()
            self.manager.current = 'uiPage1'
            self.email_input.text = ''
            self.password_input.text = ''
        else:
            print('Please enter both email and password')

class UiPage1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.5, 1, 0.5, 1)

    def update_background_color(self):
        self.background_color = (0.9, 1.0, 0.8, 1)

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
        self.manager.current = 'login_page'

class MainScreen(Screen):
    pass

class Affordemy(App):
    def build(self):
        Window.clearcolor = (0.9, 1.0, 0.8, 1)
        Window.size = (500, 650)

        sm = ScreenManager(transition=FadeTransition(duration=1.0))
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(LoginScreen(name='login_page'))
        sm.add_widget(UiPage1Screen(name='uiPage1'))

        return sm

def main():
    app = Affordemy()
    app.run()

if __name__ == '__main__':
    main()