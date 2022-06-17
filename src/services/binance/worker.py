import websocket


binance_tokens  = {
	"BTC/USDT": {
		"trigger": "more",
		"price": "60000"
	},
	"ETH/BTC": {
		"trigger": "less",
		"price": "0.07"
	},
	"DOT/USDT": {
		"trigger": "more_eq",
		"price": "40"
	},
	"ETH/USDT": {
		"trigger": "less_eq",
		"price": "4000"
	}
}


binance_tokens  = {
	"BTC/USDT": {
		"trigger": "more",
		"price": "60000"
	},
	# "ETH/BTC": {
	# 	"trigger": "less",
	# 	"price": "0.07"
	# },
	# "DOT/USDT": {
	# 	"trigger": "more_eq",
	# 	"price": "40"
	# },
	# "ETH/USDT": {
	# 	"trigger": "less_eq",
	# 	"price": "4000"
	# }
}

tokens = [ token.replace('/', '').lower() for token in binance_tokens.keys()]

print(tokens)


tokens_args_markPrice = [f"{token}@markPrice@1s" for token in tokens]



print(tokens_args_markPrice)

print("/".join(tokens_args_markPrice))

BASE_URL = "wss://fstream.binance.com"
# URL = "wss://fstream.binance.com/stream?streams=btcusdt@markPrice/btcusdt@markPrice"

MARK_PRICE_STREAM_URL = f"{BASE_URL}/stream?streams={'/'.join(tokens_args_markPrice)}"

print(MARK_PRICE_STREAM_URL)
def on_message(wsapp, message):
    print(message)


wsapp = websocket.WebSocketApp(MARK_PRICE_STREAM_URL, on_message=on_message)





wsapp.run_forever()
