
from typing import Dict, Union

class MarketSensor:
    def __init__(self, token_title: str , trigger_type: str, trigger_price: Union[float,int]) -> None:
        super().__init__()
        self._triggers_methods = {
        "less" : self._less,
        "less_eq" : self._less_eq,
        "more" : self._more,
        "more_eq" : self._more_eq,
        }
        
        assert token_title != "", "Token title should be exist"
        self.token_title = token_title
        assert trigger_type in self._triggers_methods, "Trigger is not define"
        self.trigger_type = trigger_type
        self.trigger_price = float(trigger_price)
    

        
    def _less(self, value: float) -> bool:
        # print("less")
        return value < self.trigger_price  
    
    def _less_eq(self, value: float) -> bool:
        # print("less_eq")
        return value <= self.trigger_price
    
    def _more(self, value: float) -> bool:
        # print("more")
        return value > self.trigger_price
    
    def _more_eq(self, value: float) -> bool:
        # print("more_eq")
        return value >= self.trigger_price
    
    def trigger(self, value:Union[float,int]) -> bool:
        assert isinstance(value, (float,int)) == True, f"Expected float or int type but got {type(value)}"
        return self._triggers_methods[self.trigger_type](float(value))
    
    def getName(self):
        return self.token_title
        
    def getTrigger(self):
        return f"Trigger: {self.trigger_type} price: {self.trigger_price}"
    
    def __str__(self) -> str:
        return f"Market Sensor: [TokenPair: {self.getName()}, {self.getTrigger()}]"

