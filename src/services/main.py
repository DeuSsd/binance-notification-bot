from pathlib import Path
from tools.configTools import load_config
from binance.worker import Worker





binance_config_path = Path("src\\services\\binance\\config\\config.json")
bnc = load_config(binance_config_path)

print(bnc)

import rel
Workers = []
for token_title, token_config in bnc.items():
    Workers.append(Worker(token_title,token_config))
    
for worker in Workers:
    print(worker.marketSensor)
    
for worker in Workers:
    # Calling the function `marketSensortrigger` with the argument `10`
    print(worker.marketSensor.trigger(10))




for worker in Workers:
    # Calling the function `marketSensortrigger` with the argument `10`
    worker.run_forever()

rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()
