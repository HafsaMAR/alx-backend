#!/usr/bin/env python3
""" LRUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class to implement the put and get functions
        to populate the cache_data dictionary
    """
    def __init__(self) -> None:
        super().__init__()
        # List track insertion order
        self.cache_data = OrderedDict()

    def print_cache(self):
        """ Import the super print_cache function and
            pops the least used element introduced if
            the number of elements exceeds MAX_ITEMS
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used = self.cache_data.popitem(last=False)
            print(f"DISCARD: {least_used[0]}")
        super().print_cache()

    def put(self, key, item):
        """ Puts elements in the cache_data dictionary
            if it is updated move it to the end
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value stored in the cache_data dict
            and move it to the end
        """

        if key not in self.cache_data or key is None:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
