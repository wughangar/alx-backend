#!/usr/bin/python3
"""
2. LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system and inherits from BaseCaching
    caching system does not have a limit
    """
    def __init__(self):
        super().__init__()
        self.access_tracker = []

    def put(self, key, item):
        """
        method that puts item in cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = self.access_tracker.pop(self.MAX_ITEMS - 1)
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self.access_tracker.append(key)

    def get(self, key):
        """
        method that returns value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
