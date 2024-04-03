#!/usr/bin/env python3
""" BasicCache module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class to implement the put and get functions
        to populate the cache_data dictionary
    """

    def put(self, key, item):
        """ Puts elements in the cache_data dictionary
        """
        
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value stored in the cache_data dict
        """

        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
