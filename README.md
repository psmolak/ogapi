ogapi
=====

This library is design to provide sane abstractions over OGame
statistics API to ease the process of creating parallel fetcher.


Usage
=====

```python
import ogapi

# create communities and let ogapi fetch their server lists
communities = [ogapi.Community(c) for c in ['pl', 'de', 'fr', 'en', 'us']]

# Community objects are iterables over their server lists
for server in ogapi.Community('pl'):
	print(server.url)

# to generate all resources using endpoints
endpoints = [ogapi.endpoint.players, ogapi.endpoint.alliances]

for server in chain(*communities):
	for resource in server.resources(endpoints):
		print(resource.url)

```

Using ogapi you can easily create very simple concurrent scrapper of xml files.
```python
import ogapi

# ogapi lets you easily scrap all communities and its servers
communities = [ogapi.Community(c, s) for c, s in ogapi.scrap.all()]

resources = (
	resource for resource
	in chain(*s.resources(endpoints) for s in chain(*communities))
)

for response in ogapi.utils.parallel(resources, ogapi.utils.get):
	print(response.text)
```

