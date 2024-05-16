
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
import numpy as np
import random as rn

def rnd():
    for i in range(9):
        email = ""
        chr1 = rn.randint(64, 64+22)
        chr2 = rn.randint(97, 97+22)
        passw = chr(chr1) + chr(chr2)
    for i in range(9):
        # em1 = rn.randint(64, 64+22)
        em2 = rn.randint(97, 97+22)
        emai = + chr(em2)
    return passw,emai

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
        self.orientation = 'vertical'
        self.background_color = (247/255, 247/255, 247/255, 1)
        
        # Sign in label 
        sigin_label = Label(text='[i]Sign in to Affordemy[/i]', color=(0, 0.65098039215686276, 1, 1), font_size=45, bold=True, pos_hint={'x': 0, 'y': 0.35} , markup=True, font_name='arial.ttf')
        # add the error message label to the main window, with a size of 13
        self.add_widget(sigin_label)


        self.input_fields_box = BoxLayout(size_hint=(None, None), width=500, height=280, pos_hint={'top': 1 , 'center_x': 0.5}, spacing=10)

        self.email_box = BoxLayout(size_hint=(1, None), height=140)

        self.email_label = Label(text='Email', font_size=14, color=(110/255, 110/255, 110/255, 1), bold=True, halign='left', valign='middle')
        self.email_input = TextInput(multiline=False, font_size=14, size_hint=(1, None), height=40, foreground_color=(0,0,0,1))

        self.email_box.add_widget(self.email_label)
        self.email_box.add_widget(self.email_input)

        self.password_box = BoxLayout(size_hint=(1, None), height=140)

        self.password_label = Label(text='Password', font_size=14, color=(110/255, 110/255, 110/255, 1), bold=True, halign='left', valign='middle')
        self.password_input = TextInput(multiline=False, password=True, font_size=14, size_hint=(1, None), height=40, foreground_color=(0,0,0,1))

        self.password_box.add_widget(self.password_label)
        self.password_box.add_widget(self.password_input)

        self.input_fields_box.add_widget(self.email_box)
        self.input_fields_box.add_widget(self.password_box)

        self.login_button = Button(text='Sign in', font_size=14, bold=True, size_hint=(None, None), size=(150, 50), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.autofill_button = Button(text='Autofill', font_size=14, bold=True, size_hint=(None, None), size=(150, 50), color=(0, 0, 0, 1), background_color=(0, 147, 184, 1))

        self.button_box = BoxLayout(size_hint=(None, None), width=150, height=50, pos_hint={'center_y': 0.4, 'x': 0.4})
        self.button_box.add_widget(self.login_button)

        self.add_widget(self.input_fields_box)
        self.add_widget(self.button_box)

        self.login_button.bind(on_release=self.handle_login)
        

    def handle_login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        if not email or not password:
            # create a red error message label
            error_label = Label(text='Please enter both email and password', color=(255/255, 0, 0, 1), font_size=20)
            # add the error message label to the main window, with a size of 13
            self.add_widget(error_label)
            # remove the error message label after 3 seconds
            Clock.schedule_once(lambda dt: self.remove_widget(error_label), 3)
        else:
            # create a sucesful message label
            pass_label = Label(text='Signed in', color=(0, 1, 0, 1) , font_size=17)
            # add the sucesful message label to the main window, with a size of 13
            self.add_widget(pass_label)
            # remove the sucesful message label after 3 seconds
            Clock.schedule_once(lambda dt: self.remove_widget(pass_label), 3)
            self.manager.get_screen('uiPage1').update_background_color()
            self.manager.current = 'uiPage1'
            self.email_input.text = ''
            self.password_input.text = ''


class UiPage1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.5, 1, 0.5, 1)

        # Add menu
        menu_box = BoxLayout(size_hint=(None, None), width=75, height=350, pos_hint={"y":.97  , "x": 0.}, spacing=0, orientation='horizontal')
        self.file_button = Button(text='File', font_size=19, bold=True, size_hint=(None, None), size=(50, 25), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.edit_button = Button(text='Edit', font_size=19, bold=True, size_hint=(None, None), size=(50, 20), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.help_button = Button(text='Help', font_size=19, bold=True, size_hint=(None, None), size=(50, 20), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))

        self.child_file = BoxLayout(size_hint = (None,None) , width =50 , height =150 , pos_hint ={"x":.011111  , "y":.858} , orientation = "vertical")
        self.profile_button = Button(text='Profile', font_size=13, bold=True, size_hint=(None, None), size=(40 , 20), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.courses_button = Button(text='Top Courses', font_size=11.8, bold=True, size_hint=(None, None), size=(56.5, 25.5), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.avail_button = Button(text='Availed for', font_size=12.2, bold=True, size_hint=(None, None), size=(53, 26), color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        self.payment_button = Button(text='Payment', font_size=11.8, bold=True, size_hint=(None, None), size=(45 , 20) , color=(255/255, 255/255, 255/255, 1), background_color=(0/255, 147/255, 184/255, 1))
        
        menu_box.add_widget(self.file_button)
        menu_box.add_widget(self.edit_button)
        menu_box.add_widget(self.help_button)

        self.child_file.add_widget(self.profile_button)
        self.child_file.add_widget(self.courses_button)
        self.child_file.add_widget(self.avail_button)
        self.child_file.add_widget(self.payment_button)
        
        self.add_widget(menu_box)
        self.add_widget(self.child_file)

    def handle_file_button_click(self, instance):
        self.counter = 1 - self.counter

        if self.counter == 1:
            self.add_widget(self.child_file)
            self.file_button.background_color = self.window_color
        else:
            self.remove_widget(self.child_file)
            self.file_button.background_color = self.button_color

    def update_background_color(self):
        self.background_color = (0.9, 1.0, 0.8, 1)

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image(source='Textures Logos//Affordemy_Start.png', opacity=0)
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
        Window.size = (500, 655)

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