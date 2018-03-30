import os
import time
import logging
import concurrent.futures

import requests

logger = logging.getLogger(__name__)

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)


def get(url, *args, attempts=5, cooldown=1, **kwargs):
    """Wraps requests.get with retry loop"""
    for attempt in range(attempts):
        try:
            request = requests.get(url, *args, **kwargs)
            request.raise_for_status()
            return request
        except requests.exceptions.RequestException as e:
            logger.exception('Exception occured while fetching %s', e.request)
            time.sleep(cooldown)
            cooldown *= 2

    raise RuntimeError('Attempt limit exceeded')


def parallel(iterable, action, *, executor=None, workers=20):
    """Executes action on sequence of elements in parallel"""
    executor = concurrent.futures.ThreadPoolExecutor if not executor else executor

    with executor(max_workers=workers) as e:
        futures = [e.submit(action, element) for element in iterable]
        for future in concurrent.futures.as_completed(futures):
            yield future.result()


if __name__ == "__main__":
    pass

