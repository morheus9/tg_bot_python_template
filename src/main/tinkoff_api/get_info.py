import os

from tinkoff.invest import Client

TOKEN = os.environ["TINKOFF_TOKEN"]


def main():
    with Client(TOKEN) as client:
        statuses = client.market_data.get_last_prices(instrument_id=["BBG004730N88"])
        print(statuses)


if __name__ == "__main__":
    main()
