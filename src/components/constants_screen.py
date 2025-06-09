
from textual import on
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Label
from textual.containers import Container, Center, Vertical, Middle, ScrollableContainer, Horizontal


class ContantsScreen(Screen):
    BINDINGS = [Binding('ctrl+b', 'go_back', 'Go back')]
    def __init__(self):
        super().__init__()
        self.__directories_button = Button('Directories', id='directories', classes='option_button')
        self.__files_button = Button('Files', id='files', classes='option_button')
        self.__back_button = Button('Go back', id='back', classes='option_button')

    def action_go_back(self):
        self.app.pop_screen()

    @on(Button.Pressed, '#back')
    def __on_back_button(self, event: Button.Pressed):
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        with Vertical():
            with Container(classes='background'):
                yield Header(True)
                with Center():
                    yield Label('You are on the "constants screen" so ¿What do you want to see?')
                with Center():
                    with Middle():
                        yield self.__directories_button
                        yield self.__files_button
                        yield self.__back_button
        yield Footer()
