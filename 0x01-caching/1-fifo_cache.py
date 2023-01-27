#!/usr/bin/python3
""" FIFOCache module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements the FIFO replacement policy"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key"""
        if key not in self.cache_data and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.popitem()
        print(f"DISCARD: {self.cache_data[key]}")

    def get(self, key):
        """Returns the value in self.cache_data linked to the key """
        if key is None or self.cache_data[key] is None:
            return None
        return self.cache_data[key]
