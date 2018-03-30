import concurrent.futures
from bs4 import BeautifulSoup

import utils

BASE = 'https://{}.ogame.gameforge.com'

def communities():
    """Scrap community list from ogame website."""

    r = utils.get(BASE.format('pl'))
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find(id="mmoList1").find_all('a')
    communities = [tag.get('href')[2:4] for tag in tags]

    return communities


def servers(community):
    """Scrap all servers for particular community from ogame website."""

    r = utils.get(BASE.format(community))
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find(id="serverLogin").find_all('option')
    servers = [int(tag.get('value').split('.')[0][1:-3]) for tag in tags]

    return servers


if __name__ == "__main__":
    pass

