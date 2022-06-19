# binance-notification-bot

ссылка на бота: https://t.me/binance_notificate_bot

Данный телеграмм бот присылает уведомления в телеграмм, если сработает установленный в config триггер на пару токена платформы ```Binance```

# Запуск бота
## 1 способ используя docker-compose - RECOMMENDED
1. создайте `docker-compose.yaml` со следующим содержимым, вставьте свой запишите токен в поле `TOKEN`

```docker
version: "3.3"

services:
  selected-tgbot:
    image: quteas/binance-notification-tgbot:latest
    container_name: binance-notification-tgbot
    command: bash -c "python /app/src/services/tgbot/models/createTables.py && python /app/src/main.py"
    environment:
      TOKEN: "0123456789:ABCDEFGHIABCDEFGHIJKLMNOPQRSTUVWXYZ"
      TZ: "Europe/Moscow"
    ports:
      - 80:80
      - 443:443
      - 88:88
      - 8443:8443
    volumes:
      - './database:/app/database'
      - './config:/app/src/services/binance/config'
```

2. Рядом с `docker-compose.yaml` создайте директорию ```/config```, затем в неё поместите следующий настроенный конфиг файл с необходимыми тригерами для нотификации:

```json
{
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
```


3. Запустите в оболочке shell docker контейнер для инициализации сервиса

```shell
$ docker-compose up
```

## 2 способ - используя исходный код

Для запуска бота выполните:

1. запишите токен в следующий файл `/token/telegram/token.json`

```json
{
  "TOKEN": "0123456789:ABCDEFGHIABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```
2. Следующий настроенный конфиг файл с необходимыми тригерами для нотификации поместите в файл `/src/services/binance/config/config.json`, конфиг файл имеет следующий вид:

```json
{
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
```

3. Запустите в оболочке shell инициализацию сервиса

```shell
$ python /src/services/tgbot/models/createTables.py && python /src/main.py"

```





### Links

- [Binance WebSocket APi](https://binance-docs.github.io/apidocs/delivery/en/#websocket-market-streams)