from html.parser import HTMLParser as SystemHTMLParser
from core.memory_storage import MemoryStorage
from core.type import TYPE_HEADING


class HTMLParser(SystemHTMLParser):
    storage: MemoryStorage

    def __init__(self, storage: MemoryStorage, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)

        self.storage = storage
        self.type = TYPE_HEADING

    def handle_data(self, data: str) -> None:
        if self.type == TYPE_HEADING:
            self.storage.append_heading(data)

        return super().handle_data(data)

    def feed(self, data: str, type: str) -> None:
        self.type = type

        return super().feed(data)
