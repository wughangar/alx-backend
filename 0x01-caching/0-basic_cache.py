#!/usr/bin/python3
"""
0. Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    caching system and inherits from BaseCaching
    caching system does not have a limit
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        method that puts item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        method that returns value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
