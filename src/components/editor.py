from textual.events import Key
from textual.widgets import TextArea

class Editor(TextArea):
    def __init__(self, text: str = '', language: str | None = None, id: str = None, classes: str = None):
        super().__init__(text, language=language, tab_behavior='indent', show_line_numbers=True, id=id, classes=classes)
        self.__insertions = {'(': '()', '{': '{}', '[': '[]',  '<': '<>', '\"': '""', '\'': '\'\''}

    def _on_key(self, event: Key) -> None:
        char = self.__insertions.get(event.character)
        if char:
            self.insert(char)
            self.move_cursor_relative(columns=-1)
            event.prevent_default()