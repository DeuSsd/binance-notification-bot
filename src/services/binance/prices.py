
# Import libraries
import json
import requests


# defining key/request url
BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"




{
	"BTCUSDT": {
		"trigger": "more",
		"price": "60000"
	},
	"ETHBTC": {
		"trigger": "less",
		"price": "0.07"
	},
	"DOTUSDT": {
		"trigger": "more_eq",
		"price": "40"
	},
	"ETHUSDT": {
		"trigger": "less_eq",
		"price": "4000"
	}
}



# requesting data from url
data = requests.get(key)  
data = data.json()
print(f"{data['symbol']} price is {data['price']}")