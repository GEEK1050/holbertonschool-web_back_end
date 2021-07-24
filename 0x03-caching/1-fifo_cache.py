#!/usr/bin/env python3
"""1-fifo_cache.py"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOcache:
        class that inherit from BaseCaching
        FIFO datastructure
    """
    def __init__(self):
        """constructor"""
        super().__init__()

    def get(self, key):
        """get:
            instance method: retrieve item from cache_data
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """put:
            instance method: insert item into cache_data
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                first_element_key = keys[0]
                self.cache_data.pop(first_element_key)
                print('DISCARD: {}'.format(first_element_key))
            self.cache_data[key] = item
