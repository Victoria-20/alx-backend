""" LIFOCache module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements the LIFO replacement policy"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key"""
        if key in self.cache_data:
            pop_key = self.cache_data.pop(key)
            print(f"DISCARD: {pop_key}", end='\n')
        elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(next(iter(self.cache_data)))
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to the key """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        else:
            return None
