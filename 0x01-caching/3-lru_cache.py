#!/usr/bin/python3
"""
3. LRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    caching system and inherits from BaseCaching
    caching system does not have a limit
    """
    def __init__(self):
        super().__init__()
        self.access_tracker = OrderedDict()

    def put(self, key, item):
        """
        method that puts item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        self.access_tracker.pop(key, None)
        self.access_tracker[key] = None

        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key = next(iter(self.access_tracker))
            del self.cache_data[lru_key]
            del self.access_tracker[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        method that returns value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
