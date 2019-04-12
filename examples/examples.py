from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()

# List coins
client.coins()

# Get coin by ID (example: btc-bitcoin)
client.coin("btc-bitcoin")

# Get tweets by coin ID (max 50 tweets)
client.twitter("btc-bitcoin")

# Get coin events by coin ID
client.events("btc-bitcoin")

# Get exchanges by coin ID
client.exchanges("btc-bitcoin")

# Get markets by coin ID (USD,BTC,ETH,PLN)
client.markets("btc-bitcoin", quotes="USD")

# Get 24h OHLC candle (USD,BTC)
client.candle("btc-bitcoin")

# Get historical OHLCV information for a specific coin (USD,BTC)
client.candles("btc-bitcoin", start="2019-01-11T00:00:00Z")

# Get today OHLC (can change every each request until actual close of the day at 23:59:59)
client.today("btc-bitcoin")

# Get people by ID (example: vitalik-buterin)
client.people("vitalik-buterin")

# List tags
client.tags()

client.tags(additional_fields="coins,icos")

# Get tag by ID
client.tag("blockchain-service")

# Get tickers for all coins (USD,BTC,ETH)
client.tickers()

# Get ticker information for a specific coin (USD,BTC,ETH)
client.ticker("btc-bitcoin")

# Get historical ticker information for a specific coin (USD,BTC,ETH)
client.historical("btc-bitcoin", start="2019-04-11T00:00:00Z")

# List exchanges
client.exchange_list()

# Get exchange by ID
client.exchange("binance", quotes="USD")

# Get markets by exchange ID (USD,BTC,ETH,PLN) with quotes USD
client.exchange_markets("binance", quotes="USD")

# Search
client.search(q="btc",c="currencies,exchanges,icos,people,tags", modifier="symbol_search", limit=42)

# Price converter
client.price_converter(base_currency_id="btc-bitcoin", quote_currency_id="usd-us-dollars", amount=1337)
