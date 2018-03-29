ogapi
=====

This library is design to provide sane abstractions over OGame
statistics API to ease the process of creating parallel fetcher.


Usage
=====

```python
import ogapi

endpoints = [ogapi.players, ogapi.alliances] + ogapi.highscores
server = ogapi.Server('pl', 151)

for resource in gather(server, endpoints):
	print(resource.url)
```
