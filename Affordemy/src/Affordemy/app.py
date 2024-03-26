"""
Application to upload different paid courses 
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from android_application.interface import (
    MainScreen,
    AboutScreen,
    SettingsScreen,
)

class AndroidApplication(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.screen_manager = toga.ScreenManager()

        # Add screens
        self.screen_manager.add(MainScreen(name='main'))
        self.screen_manager.add(AboutScreen(name='about'))
        self.screen_manager.add(SettingsScreen(name='settings'))

        # Set the main screen
        self.screen_manager.current = 'main'

        main_box = toga.Box()
        main_box.add(self.screen_manager)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return AndroidApplication()
