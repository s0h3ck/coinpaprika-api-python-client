import pytest
import requests_mock

from coinpaprika import client as Coinpaprika
from coinpaprika.exceptions import CoinpaprikaAPIException
from coinpaprika.exceptions import CoinpaprikaRequestException

client = Coinpaprika.Client()

def test_invalid_request():

    with pytest.raises(CoinpaprikaRequestException):
        with requests_mock.mock() as m:
            m.get("https://api.coinpaprika.com/v1/coins", text="invalid")
            client.coins()


def test_api_exception():

    with pytest.raises(CoinpaprikaAPIException):
        with requests_mock.mock() as m:
            json_obj = {"error": "<error message>"}
            m.get("https://api.coinpaprika.com/v1/coins/btc", json=json_obj, status_code=400)
            client.coin("btc")

def test_api_exception_invalid_json():

    with pytest.raises(CoinpaprikaAPIException):
        with requests_mock.mock() as m:
            fake_json_obj = "invalid"
            m.get("https://api.coinpaprika.com/v1/coins/btc", json=fake_json_obj, status_code=400)
            client.coin("btc")

def test_api_exception_with_no_json():

    with pytest.raises(CoinpaprikaAPIException):
        with requests_mock.mock() as m:
            m.get("https://api.coinpaprika.com/v1/coins/btc", status_code=400)
            client.coin("btc")
