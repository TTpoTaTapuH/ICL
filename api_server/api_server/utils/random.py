from django.utils.timezone import now
from typing import Set, Optional, Iterable
import random
from .base64 import pack_structure

_MAX_UINT32 = 0xFFFFFFFF
_MAX_RETRY_ON_SAME = 10
_MAX_INCREMENT_ON_SAME = 100


class TooManyRetries(Exception):
    pass


def random_int_in_range(min_value: int, max_value: int,
                        not_equal: Optional[Set]=None,
                        max_retry_on_same: Optional[int]=None, max_increment_on_same: Optional[int]=None) -> int:
    """
    Returns random integer in a given range
    Note: max_retry_on_same and max_increment_on_same multiply by each other
    :param min_value: start of a range
    :param max_value: end of a range
    :param not_equal: numbers to avoid
    :param max_retry_on_same: retry count on same value
    :param max_increment_on_same: increment after retry count on same value
    :return: random number
    :raise TooManyRetries: max_retry_on_same x max_increment_on_same reached with no success
    """

    n = random.randint(min_value, max_value)
    if not_equal:
        max_retry_on_same = max_retry_on_same if max_retry_on_same is not None else _MAX_RETRY_ON_SAME
        max_increment_on_same = max_increment_on_same if max_increment_on_same is not None else _MAX_INCREMENT_ON_SAME
        retries = 0
        while n in not_equal and retries < max_retry_on_same:
            n = random.randint(0, _MAX_UINT32)
            retries += 1
            increments = 0
            while n in not_equal and increments < max_increment_on_same:
                increments += 1
                n = n + 1 if n < max_value else min_value
        if n in not_equal:
            raise TooManyRetries('Cannot find suitable random number')
    return n


def random_uint32(not_equal: Optional[Set]=None,
                  max_retry_on_same: Optional[int]=None, max_increment_on_same: Optional[int]=None) -> int:
    """
    Returns random integer in unsigned int32 range
    Note: max_retry_on_same and max_increment_on_same multiply by each other
    :param not_equal: numbers to avoid
    :param max_retry_on_same: retry count on same value
    :param max_increment_on_same: increment after retry count on same value
    :return: random number
    :raise TooManyRetries: max_retry_on_same x max_increment_on_same reached with no success
    """

    return random_int_in_range(0, _MAX_UINT32, not_equal, max_retry_on_same, max_increment_on_same)


def random_unique_uint32_generator() -> Iterable[int]:
    """
    Generates random integers sequence in unsigned int32 range
    :return: random numbers sequence generator
    :raise TooManyRetries: max_retry_on_same x max_increment_on_same reached with no success
    """
    not_equal = set()
    while True:
        n = random_uint32(not_equal)
        not_equal.add(n)
        yield n


def timestamp_random_base64(url_safe=False, random_part=None, timestamp=None):
    if timestamp is None:
        timestamp = round(now().timestamp())
    if random_part is None:
        random_part = random_uint32()
    return pack_structure(timestamp, random_part, url_safe=url_safe, structure_pattern='<QL', decode_encoding='ASCII')

