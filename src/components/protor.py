from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Footer, Header, Button
from textual.containers import Vertical, Center, Middle, Container

from src.components.input_screen import InputScreen
from src.components.alert_screen import AlertScreen
from src.components.warning_screen import WarningScreen
from src.components.editor_screen import EditorScreen

from src.classes.file import File
from src.classes.directory import Directory

class Protor(App):
    CSS_PATH = '../../css/protor.tcss'
    def __init__(self):
        super().__init__()
        self.__proyect_button = Button('New proyect', id='new_proyect', classes='option_button')
        self.__schemas_button = Button('Schemas', id='schemas', classes='option_button')
        self.__constants_button = Button('Constants', id='constants', classes='option_button')
        self.__config_button = Button('Configs', id='config', classes='option_button')        
        self.__exit_button = Button('Exit', id='exit', classes='option_button')
        self.__file = File('protor.py')

    def __set_title(self): self.title = Protor.__name__

    @on(Button.Pressed, '#new_proyect')
    def __on_pressed_new_proyect(self):
        self.push_screen(EditorScreen(self.__file))
        self.__set_title()

    @on(Button.Pressed, '#exit')
    def __on_pressed_exit(self, event: Button.Pressed):
        self.push_screen(WarningScreen('¿Exit?'), self.__exit)

    def __exit(self, quit_app: bool):
        if quit_app:
            self.app.exit()

    def compose(self) -> ComposeResult:
        with Vertical():
            with Container(classes='background'):
                yield Header(True)
                with Center():
                    yield Label('Welcome again to Protor')
                    with Middle():
                        yield self.__proyect_button
                        yield self.__schemas_button
                        yield self.__constants_button
                        yield self.__config_button
                        yield self.__exit_button
        yield Footer()
