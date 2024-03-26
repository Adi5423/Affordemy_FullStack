import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MainScreen(toga.App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Add a button to the main screen
        self.button = toga.Button(
            "Click me!",
            on_press=self.on_button_click
        )
        self.main_box.add(self.button)

        # Add a button to the main screen
        self.button = toga.Button(
            "By the Dev!!",
            on_press=self.on_button_click
        )
        self.main_box.add(self.button)

    def on_button_click(self, widget):
        print("Button was clicked!")

class AboutScreen(toga.App):
    pass

class SettingsScreen(toga.App):
    pass

class AndroidApplication(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.screen_manager = toga.Stack(style=Pack(direction=COLUMN))

        # Add screens
        self.main_screen = MainScreen(name='main')
        self.about_screen = AboutScreen(name='about')
        self.settings_screen = SettingsScreen(name='settings')

        self.screen_manager.add(self.main_screen)
        self.screen_manager.add(self.about_screen)
        self.screen_manager.add(self.settings_screen)

        # Set the main screen
        self.screen_manager.current = self.main_screen

        main_box = toga.Box()
        main_box.add(self.screen_manager)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return AndroidApplication()