class CoinpaprikaAPIException(Exception):

    def __init__(self, response):
        self.code = 0

        try:
            json_response = response.json()
        except ValueError:
            self.message = "JSON error message from Coinpaprika: {}".format(response.text)
        else:
            if "error" not in json_response:
                self.message = "Wrong json format from CoinpaprikaAPI"
            else:
                self.message = json_response["error"]

        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return "CoinpaprikaAPIException(status_code: {}): {}".format(self.status_code, self.message)

class CoinpaprikaRequestException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "CoinpaprikaRequestException: {}".format(self.message)
