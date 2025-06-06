from textual import on
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Label
from textual.containers import Container, Center, Vertical, Middle

class NewProyectScreen(Screen):
    def __init__(self):
        super().__init__()