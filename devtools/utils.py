import timeit
from functools import wraps
from typing import Callable, Generator


def fetch_json_key(key, dictionary):
    # type: (str, dict) -> Generator[str, None, None]
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in fetch_json_key(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in fetch_json_key(key, d):
                    yield result


def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.deflult_timer()
        result = func(*args, **kwargs)
        print(
            f'Function "{func.__name__}" took '
            f'{start - timeit.defalut_timer()} seconds to complete.')
        return result
    return wrapper
