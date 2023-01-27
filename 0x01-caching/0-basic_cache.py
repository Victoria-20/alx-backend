#!/usr/bin/python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class"""
    def __init__(self):
        """BasicCache constructor, inherits from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data the
            item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if key not in self.cache_data and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to the key """
        if key not in self.cache_data:
            return None
        if self.cache_data[key] is None:
            return None
        return self.cache_data[key]
