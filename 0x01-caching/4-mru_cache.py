#!/usr/bin/env python3
""" MRUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class to implement the put and get functions
        to populate the cache_data dictionary
    """
    def __init__(self) -> None:
        super().__init__()
        # List track insertion order
        self.cache_data = OrderedDict()

    def print_cache(self):
        """ Import the super print_cache function
        """
        super().print_cache()

    def put(self, key, item):
        """ Puts elements in the cache_data dictionary
            if it is updated move it to the end pop the last one
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_added_key, last_added_value = self.cache_data.popitem()
                most_used = self.cache_data.popitem()
                self.cache_data[last_added_key] = last_added_value
                print(f"DISCARD: {most_used[0]}")

    def get(self, key):
        """ Retrieves the value stored in the cache_data dict
            and move it to the end
        """

        if key not in self.cache_data or key is None:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
