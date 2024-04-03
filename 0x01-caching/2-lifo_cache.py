#!/usr/bin/env python3
""" LIFOCache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class to implement the put and get functions
        to populate the cache_data dictionary
    """
    def __init__(self) -> None:
        super().__init__()
        # List track insertion order
        self.insertion_order = []

    def print_cache(self):
        """ Import the super print_cache function and
            pops the first element introduced if the number
            of elements exceeds MAX_ITEMS
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(
                self.insertion_order[BaseCaching.MAX_ITEMS - 1])
            print(
                f"DISCARD: {self.insertion_order[BaseCaching.MAX_ITEMS - 1]}"
                )
            del self.insertion_order[BaseCaching.MAX_ITEMS - 1]
        super().print_cache()

    def put(self, key, item):
        """ Puts elements in the cache_data dictionary
        """
        if key and item:
            if key in self.cache_data.keys():
                index = self.insertion_order.index(key)
                key = self.insertion_order.pop(index)
            self.cache_data[key] = item
            self.insertion_order.append(key)

    def get(self, key):
        """ Retrieves the value stored in the cache_data dict
        """

        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
