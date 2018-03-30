import itertools
import urllib.parse
from datetime import timedelta


class Endpoint:
    """
    Stores information about particular endpoint such as name or
    update timedelta.
    """

    def __init__(self, path, delta, data=None):
        self.path = path
        self.delta = delta
        self.data = data

    @property
    def seconds(self):
        return self.delta.total_seconds()

    def encode(self):
        """
        Encodes itself as url path.
        """
        query = '?' + urllib.parse.urlencode(self.data) if self.data else ''
        return self.path + query


def playerdata(ids):
    """
    playerData endpoint is provided as a function that takes iterable
    of ids of players and returns generator of all Endpoints.
    """
    return (
        Endpoint('playerData.xml', timedelta(days=7), {'id': id})
        for id in ids
    )

players = Endpoint('players.xml', timedelta(days=1))
alliances = Endpoint('alliances.xml', timedelta(days=1))
universe = Endpoint('universe.xml', timedelta(days=7))
universes = Endpoint('universes.xml', timedelta(days=1))
serverdata = Endpoint('serverData.xml', timedelta(days=1))
highscores = [
    Endpoint('highscore.xml', timedelta(hours=1), {'category': c, 'type': t})
    for c, t in itertools.product([1, 2], range(8))
]

if __name__ == "__main__":
    pass

