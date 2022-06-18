import unittest

from .trigers import MarketSensor


class TestStringMethods(unittest.TestCase):


    def test_empty_initialization(self):
        token = 'BTC/USDT'
        target_price = '60000'

        with self.assertRaises(AssertionError):
            token_noName = MarketSensor("", "", target_price)
        with self.assertRaises(AssertionError):
            token_noTrigger =  MarketSensor(token, "", target_price)
        with self.assertRaises(AssertionError):
            token_falseTrigger =  MarketSensor(token, "less_then", target_price)
        with self.assertRaises(AssertionError):
            token_falseTrigger =  MarketSensor(token, 2 , target_price)
        
        
    def test_triggers(self):
        token = 'BTC/USDT'
        target_price = 10
        # triggers = [
            # 'more',
            # 'more_eq',
            # 'less',
            # 'less_eq',
            # ]
        
        trigger_more =  MarketSensor(token, trigger_type="more", trigger_price = float(target_price))
        trigger_more_eq =  MarketSensor(token, trigger_type="more_eq", trigger_price = float(target_price))
        trigger_less =  MarketSensor(token, trigger_type="less", trigger_price = float(target_price))
        trigger_less_eq =  MarketSensor(token, trigger_type="less_eq", trigger_price = float(target_price))
        
        self.assertTrue(trigger_more.trigger(target_price+1))
        self.assertFalse(trigger_more.trigger(target_price))
        self.assertFalse(trigger_more.trigger(target_price-1))
        
        self.assertTrue(trigger_more_eq.trigger(target_price+1))
        self.assertTrue(trigger_more_eq.trigger(target_price))
        self.assertFalse(trigger_more_eq.trigger(target_price-1))
        
        self.assertFalse(trigger_less.trigger(target_price+1))
        self.assertFalse(trigger_less.trigger(target_price))
        self.assertTrue(trigger_less.trigger(target_price-1))
        
        self.assertFalse(trigger_less_eq.trigger(target_price+1))
        self.assertTrue(trigger_less_eq.trigger(target_price))
        self.assertTrue(trigger_less_eq.trigger(target_price-1))
        
        with self.assertRaises(AssertionError):
            self.assertTrue(trigger_less_eq.trigger("sdsd"))
        
        
if __name__ == '__main__':
    unittest.main()
