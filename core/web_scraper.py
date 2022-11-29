from core.fetcher import FetchResult
from core.html_parser import HTMLParser
from core.memory_storage import MemoryStorage
from core.type import TYPE_HEADING

WEB_OPENTAG_H2 = "<h2>"
WEB_ENDTAG_H2 = "</h2>"


class WebScraper(object):
    r: FetchResult
    storage: MemoryStorage

    def __init__(self, r: FetchResult, storage: MemoryStorage) -> None:
        self.r = r
        self.storage = storage

    def _find_text(self, sub: str, start: int = 0):
        return self.r.data.find(sub, start)

    def get_headings(self):
        opentag_index = self._find_text(WEB_OPENTAG_H2)
        endtag_index = self._find_text(WEB_ENDTAG_H2, opentag_index)

        htmlparser = HTMLParser(self.storage)
        while opentag_index >= 0 and endtag_index >= 0:
            data = self.r.data[opentag_index:endtag_index]
            htmlparser.feed(data, TYPE_HEADING)

            opentag_index = self._find_text(WEB_OPENTAG_H2, endtag_index + 1)
            endtag_index = self._find_text(WEB_ENDTAG_H2, opentag_index)

        return self.storage.get_heading()
