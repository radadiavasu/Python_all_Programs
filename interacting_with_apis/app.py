from libs.openexchange import OpenExchangeClient
import time

start = time.time()
APP_ID = "508732fc366f4e61bc55420edf247eea"
client = OpenExchangeClient(APP_ID)
end  = time.time()

print(end - start)
usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f"USD{usd_amount} is GBP{gbp_amount}")


#############################################################
# Program : 1
#############################################################
# import requests

# APP_ID = "508732fc366f4e61bc55420edf247eea"
# ENDPOINT = "https://openexchangerates.org/api/latest.json"

# response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# exchange_rates = response.json()["rates"]

# usd_amount = 1000
# gbp_amount = usd_amount * exchange_rates["GBP"]

# print(f"USD{usd_amount} is GBP{gbp_amount}")