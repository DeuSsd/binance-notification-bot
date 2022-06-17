


# from abc import ABC




# class BasePair(ABC): 
class MarketSensor:
    def __init__(self, title, trigger_type, trigger_price) -> None:
        super().__init__()
        self._title = title
        self.token = title.replace('/', '').lower()
        self.trigger_type = trigger_type
        self.trigger_price = float(trigger_price)
    
   
        
    def _less(self, value):
        print("less")
        return value < self.trigger_price  
    
    def _less_eq(self, value):
        print("less_eq")
        return value <= self.trigger_price
    
    def _more(self, value):
        print("more")
        return value > self.trigger_price
    
    def _more_eq(self, value):
        print("more_eq")
        return value >= self.trigger_price
    
    def trigger(self, value):  
        triggers = {
            "less" : self._less,
            "less_eq" : self._less_eq,
            "more" : self._more,
            "more_eq" : self._more_eq,
        }
        
        return triggers[self.trigger_type](value)
    
    def getName(self):
        return self._title
        
    def getTrigger(self):
        return f"Trigger: {self.trigger_type} price: {self.trigger_price}"
    
    def __str__(self) -> str:
        return f"Market Sensor: [TokenPair: {self.getName()}, {self.getTrigger()}]"
    
    
if __name__ == "__main__":
    bnc = {
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


    Workers = []
    for token, token_config in bnc.items():
        title=token
        trigger_type=token_config.get("trigger")
        trigger_price=token_config.get("price")
        print(title,trigger_type,trigger_price)
        Workers.append(MarketSensor(title,trigger_type,trigger_price))
        
    for worker in Workers:
        print(worker)
        
    for worker in Workers:
        print(worker.trigger(10))