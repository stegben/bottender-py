# bottender-py

[![travis-ci][travis-image]][travis-url]    [![pypi-version][pypi-image]][pypi-url]    [![codecov][codecov-image]][codecov-url]

[travis-image]: https://travis-ci.org/stegben/bottender-py.svg?branch=master
[travis-url]: https://travis-ci.org/stegben/bottender-py

[pypi-image]: https://badge.fury.io/py/bottender-py.svg
[pypi-url]: https://badge.fury.io/py/bottender-py

[codecov-image]: https://codecov.io/gh/stegben/bottender-py/branch/master/graph/badge.svg
[codecov-url]: https://codecov.io/gh/stegben/bottender-py

Rewrite the famous bot framework [Bottender](https://bottender.js.org/) in async python. All credits should be back to [Yoctol Info](https://www.yoctol.com/).


# The following part is not ready yet, plz don't take them seriously


## Installation
```bash
pip install bottender
```


## Usage

```python
from bottender import MessengerBot

bot = MessengerBot(
    access_token="__access_token__",
    app_secret="__app_secret__",
)

@bot.on_event
async def echo_handler(context):
    if context.event.is_text:
        await context.send_text('')


# or
# >>> bot.on_event(handler)
```


## Supported frameworks

- Sanic
First, prepare a :
```
```

Or, use `blueprint` for larger project:
```python
from sanic import Sanic
from bottender.sanic import create_blueprint

bot = ...

bp = create_blueprint(bot, name='bot', url_prefix='/bot')
app = Sanic(__name__)
app.blueprint(bp)
```

or, use ``

- aiohttp
Use route hadler.
```python
```
