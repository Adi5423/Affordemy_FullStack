import toga

class MainScreen(toga.Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add a button to the main screen
        self.button = toga.Button(
            "Click me!",
            on_press=self.on_button_click
        )
        self.main_box.add(self.button)

    def on_button_click(self, widget):
        print("Button was clicked!")