#!/usr/bin/python3
"""
1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key, discard_value = next(iter(self.cache_data.items()))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        method that returns value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
