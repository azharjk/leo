from typing import List


class MemoryStorage(object):
    headings: List[str]

    def __init__(self) -> None:
        self.headings = []

    def append_heading(self, s: str) -> None:
        self.headings.append(s)

    def get_heading(self) -> List[str]:
        return self.headings
