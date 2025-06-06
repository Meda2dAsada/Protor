from textual import on
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Input
from textual.containers import Horizontal, Container

class InputScreen(ModalScreen):

    BINDINGS = [Binding('ctrl+c', 'cancel_message', 'Cancel')]
    AUTO_FOCUS = '#data_input'

    def __init__(self, message: str, is_optional: bool = False):
        super().__init__()
        self.__is_optional = is_optional
        self.__data_input = Input(placeholder=message, id= 'data_input')
        self.__accept = Button.success('Accept', id= 'accept', disabled=not self.__is_optional)
        self.__cancel = Button.error('Cancel', id= 'cancel')
        self.__footer = Footer()

    def compose(self):

        with Container():
            yield self.__data_input
            with Horizontal():
                yield self.__accept
                yield self.__cancel
        yield self.__footer

    @on(Input.Changed, '#data_input')
    @on(Input.Submitted, '#data_input')
    def set_input(self, event: Input.Changed | Input.Submitted):
        data = event.value.strip()
        button: Button = self.query_one('#accept', Button)

        if not self.__is_optional:
            if data:
                button.disabled = False
            else:
                button.disabled = True

    @on(Button.Pressed)
    def __on_quit_screen(self, event: Button.Pressed):
        self.dismiss(self.__data_input.value)

    def action_cancel_message(self):
        self.dismiss(False)