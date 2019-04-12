import requests

from coinpaprika.exceptions import CoinpaprikaAPIException
from coinpaprika.exceptions import CoinpaprikaRequestException

class Client(object):
    API_URL = "https://api.coinpaprika.com/v1"

    def __init__(self, requests_params=None):
        self.session = self._init_session()
        self._requests_params = requests_params
    
    def _init_session(self):
        session = requests.session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'coinpaprika/python'})
        return session

    def _request(self, method, uri, force_params=False, **kwargs):

        kwargs['timeout'] = 10

        data = kwargs.get('data', None)
        if data and isinstance(data, dict):
            kwargs['data'] = data

        # if get request assign data array to params value for requests lib
        if data and (method == 'get' or force_params):
            kwargs['params'] = kwargs['data']
            del(kwargs['data'])

        response = getattr(self.session, method)(uri, **kwargs)

        return self._handle_response(response)

    def _create_api_uri(self, path):
        return "{}/{}".format(self.API_URL, path)

    def _request_api(self, method, path, **kwargs):
        uri = self._create_api_uri(path)
        return self._request(method, uri, **kwargs)

    def _handle_response(self, response):
        if not str(response.status_code).startswith('2'):
            raise CoinpaprikaAPIException(response)
        try:
            return response.json()
        except ValueError:
            raise CoinpaprikaRequestException("Invalid Response: {}".format(response.text))

    def _get(self, path, **kwargs):
        return self._request_api('get', path, **kwargs)

    def global_market(self):
        return self._get("global")

    def coins(self):
        return self._get("coins")

    def coin(self, coin_id):
        return self._get("coins/{}".format(coin_id))

    def twitter(self, coin_id):
        return self._get("coins/{}/twitter".format(coin_id))

    def events(self, coin_id):
        return self._get("coins/{}/events".format(coin_id))

    def exchanges(self, coin_id):
        return self._get("coins/{}/exchanges".format(coin_id))

    def markets(self, coin_id, **params):
        return self._get("coins/{}/markets".format(coin_id), data=params)

    def candle(self, coin_id, **params):
        return self._get("coins/{}/ohlcv/latest".format(coin_id), data=params)

    def candles(self, coin_id, **params):
        return self._get("coins/{}/ohlcv/historical".format(coin_id), data=params)

    def today(self, coin_id, **params):
        return self._get("coins/{}/ohlcv/today".format(coin_id), data=params)

    def people(self, person_id):
        return self._get("people/{}".format(person_id))

    def tags(self, **params):
        return self._get("tags", data=params)

    def tag(self, tag_id, **params):
        return self._get("tags/{}".format(tag_id), data=params)

    def tickers(self, **params):
        return self._get("tickers", data=params)

    def ticker(self, coin_id, **params):
        return self._get("tickers/{}".format(coin_id), data=params)

    def historical(self, coin_id, **params):
        return self._get("tickers/{}/historical".format(coin_id), data=params)

    def exchange_list(self, **params):
        return self._get("exchanges", data=params)

    def exchange(self, exchange_id, **params):
        return self._get("exchanges/{}".format(exchange_id), data=params)

    def exchange_markets(self, exchange_id, **params):
        return self._get("exchanges/{}/markets".format(exchange_id), data=params)

    def search(self, **params):
        return self._get("search", data=params)

    def price_converter(self, **params):
        return self._get("price-converter", data=params)
