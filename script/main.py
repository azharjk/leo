from core.fetcher import Fetcher


def main():
    r = Fetcher.Get("")
    print(r.data)


if __name__ == "__main__":
    main()
