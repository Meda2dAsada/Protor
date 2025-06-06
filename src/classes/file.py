from src.constants.const import FILE
from src.classes.system_entry import SystemEntry
from src.classes.system_creator import SystemCreator

class File(SystemEntry):

    def __init__(self, name: str, path: str = None, content: str | None = None):
        super().__init__(name, path, FILE)
        self.__content: str = None
        self.__split_name = None
        self.set_content(content)
        self.__set_extension(name)

    def get_split_name(self): return self.__split_name
    
    def __set_extension(self, name: str):
        self.__split_name = SystemCreator.trim_file(name)

    def write_self(self):
        SystemCreator.write_entry(self.get_absolute_path(), self.get_content(), self.get_entry_type())

    def set_content(self, content: str):
        if self.validate_strings(content):
            self.__content = content
        else:
            self.__content = ''

    def get_content(self): return self.__content
