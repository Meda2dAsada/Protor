from textual import on
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header
from textual.containers import Container, Center, Vertical, Middle

from src.components.editor import Editor
from src.components.warning_screen import WarningScreen

from src.classes.file import File

class EditorScreen(Screen):
    BINDINGS = [Binding('ctrl+s', 'save', 'Save'), Binding('ctrl+l', 'leave', 'Leave')]
    def __init__(self, file: File):
        super().__init__()
        self.__file = file
        self.__editor = Editor(self.__file.get_content(), id='editor')
        self.__is_saved = True
        self.__header = Header(True)
        self.__set_title()

    def compose(self):
        with Vertical():
            with Container(classes='background'):
                yield self.__header
                with Center():
                    with Middle():
                        yield self.__editor
                        yield Footer()


    def __set_title(self):
        self.title = f'{self.__file.get_name()} @ {'Saved  ' if self.__is_saved else 'Unsaved'}'

    @on(Editor.Changed, '#editor')
    def __on_editor_changed(self, event: Editor.Changed):
        if self.__file.get_content() != self.__editor.text:
            self.__is_saved = False
        else:
            self.__is_saved = True

        self.__set_title()

    def action_save(self):
        self.__is_saved = True
        self.__file.set_content(self.__editor.text)
        self.__set_title()
    
    def action_leave(self):
        if not self.__is_saved:
            self.app.push_screen(WarningScreen('¿Leave editing? Changes are unsaved'), self.__leave_unsaved)
        self.dismiss()

    def __leave_unsaved(self, quit_warning: bool):
        if quit_warning:
            self.dismiss()
