#!/usr/bin/python3
""" LRUCache module """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements the LRU replacement policy"""
    def __init__(self) -> None:
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key"""
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # remove old item from the cache
                old_key = self.keys_queue.pop(0)
                print(f"DISCARD: {old_key}", end='\n')
                del self.cache_data[old_key]
        # append the new item to tha cached_data
        self.cache_data[key] = item
        self.keys_queue.append(key)

    def get(self, key):
        """Returns the value in self.cache_data linked to the key """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
