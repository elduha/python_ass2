from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
crp = cg.get_coins_markets(vs_currency='usd')
print(crp)

