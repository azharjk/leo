import sys
from core.fetcher import Fetcher
from core.web_scraper import WebScraper
from core.memory_storage import MemoryStorage


def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: need to provide the url", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    r = Fetcher.Get(url)

    scraper = WebScraper(r, MemoryStorage())

    print(scraper.get_headings())


if __name__ == "__main__":
    main()
