from core.fetcher import FetchResult
from core.html_parser import HTMLParser
from core.memory_storage import MemoryStorage
from core.type import TYPE_HEADING
from core.web_tag import *


class WebScraper(object):
    r: FetchResult
    storage: MemoryStorage

    def __init__(self, r: FetchResult, storage: MemoryStorage) -> None:
        self.r = r
        self.storage = storage

    def _find_text(self, sub: str, start: int = 0):
        return self.r.data.find(sub, start)

    def _get_headings_impl(self, opentag: str, endtag: str):
        opentag_index = self._find_text(opentag)
        endtag_index = self._find_text(endtag, opentag_index)

        htmlparser = HTMLParser(self.storage)
        while opentag_index >= 0 and endtag_index >= 0:
            data = self.r.data[opentag_index:endtag_index]
            htmlparser.feed(data, TYPE_HEADING)

            opentag_index = self._find_text(opentag, endtag_index + 1)
            endtag_index = self._find_text(endtag, opentag_index)

    def get_headings(self):
        for i in range(len(WEB_OPENTAG_HEADING_LIST)):
            self._get_headings_impl(
                WEB_OPENTAG_HEADING_LIST[i], WEB_ENDTAG_HEADING_LIST[i]
            )

        return self.storage.get_headings()
