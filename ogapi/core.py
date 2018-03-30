from itertools import product
from collections import namedtuple

from . import scrap
from . import endpoint


BASE = 'https://s{}-{}.ogame.gameforge.com'


class Server:
    def __init__(self, number, country):
        self.number = number
        self.country = country

    @property
    def url(self):
        return BASE.format(self.number, self.country)

    def resources(self, endpoints):
        for endpoint in endpoints:
            url = self.url + '/api/' + endpoint.encode()
            yield Resource(url, endpoint, self)

    def __str__(self):
        return 's{}-{}'.format(self.number, self.country)


class Community:
    def __init__(self, country, servers=None):
        self.country = country
        self.servers = [
            Server(s, country) for s
            in (servers if servers is not None else scrap.servers(country))
        ]

    def __iter__(self):
        return self.servers.__iter__()

    def resources(self, endpoints):
        for server in self.servers:
            for resource in server.resources(endpoints):
                yield resource


Resource = namedtuple('Resource', ['url', 'endpoint', 'server'])
Resource.__doc__ += ': Represents resource for concrete endpoint and server'
Resource.url.__doc__ = 'Full url for resource'
Resource.server.__doc__ = 'Assosiated server object'
Resource.endpoint.__doc__ = 'Assosiated endpoint object'


if __name__ == "__main__":
    pass

