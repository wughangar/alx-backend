#!/usr/bin/python3
"""
5. LFU Caching
"""
from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU (Least Frequently Used) caching system inheriting from BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.frequency_counter = defaultdict(int)
        self.access_tracker = OrderedDict()

    def put(self, key, item):
        """
        Method that puts item in cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        self.access_tracker.pop(key, None)
        self.access_tracker[key] = None

        self.frequency_counter[key] += 1

        if len(self.cache_data) > self.MAX_ITEMS:
            min_frequency = min(self.frequency_counter.values())
            least_frequent_keys = [k for k, v in
                                   self.frequency_counter.items()
                                   if v == min_frequency]

            lru_key = None
            if len(least_frequent_keys) > 1:
                lru_key = next(iter(self.access_tracker))

                for key in least_frequent_keys:
                    if lru_key is None or (key in self.access_tracker
                                           and self.access_tracker[key]
                                           is not None and
                       (self.access_tracker[lru_key] is None or
                           self.access_tracker[key] < self.access_tracker
                           [lru_key])):
                        lru_key = key

            discard_key = lru_key if lru_key else least_frequent_keys[0]
            del self.cache_data[discard_key]
            del self.access_tracker[discard_key]
            del self.frequency_counter[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        Method that returns value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_tracker.pop(key, None)
        self.access_tracker[key] = None

        self.frequency_counter[key] += 1

        return self.cache_data[key]
