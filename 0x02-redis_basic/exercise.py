#!/usr/bin/env python3
"""Writing strings to redis"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Class cache data in redis
    """
    def __init__(self):
        """
        initilaize data
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method that takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
