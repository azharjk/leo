import sys
from core.fetcher import Fetcher


def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: need to provide the url", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    r = Fetcher.Get(url)
    print(r.data)


if __name__ == "__main__":
    main()
