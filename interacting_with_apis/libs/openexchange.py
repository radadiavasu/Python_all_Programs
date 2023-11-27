import requests
# import functools
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"
    
    def __init__(self, app_id):
        self.app_id = app_id
      
    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    # @functools.lru_cache(maxsize=2) # 1."lru" means list recently used. 2."catch" means piece of storage that keeps data temporarily.  
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()
    
    def convert(self, from_account, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]
        
        if from_currency == "USD":
            return from_account * to_rate
        else:
            from_in_usd = from_account / rates[from_currency]
            return from_in_usd * to_rate