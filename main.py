import requests
import time
from market_addresses import ship_market_addresses

dexlab_endpoint = "https://open-api.dexlab.space"

dexlab_orderbook_endpoint = "https://open-api.dexlab.space/v1/orderbooks"

dexlab_market_price_endpoint = "https://open-api.dexlab.space/v1/prices/:DLDLMrzumzFSJUub5we5rNTymLtUsnvmRw281pj9wxc9/last"


PX6_MARKET_ADDRESS_USDC = "DLDLMrzumzFSJUub5we5rNTymLtUsnvmRw281pj9wxc9"
PX5_MARKET_ADDRESS_USDC = "3ySaxSspDCsEM53zRTfpyr9s9yfq9yNpZFXSEbvbadLf"


for ship in ship_market_addresses:
    USDC_adr = ship_market_addresses[ship]["USDC"]
    ATLAS_adr = ship_market_addresses[ship]["ATLAS"]
    if len(USDC_adr) > 0:
        response = requests.get(url=f"{dexlab_orderbook_endpoint}/{USDC_adr}")
        try:
            highest_buy = response.json()["data"]["bids"][-1]
        except IndexError:
            highest_buy = "There are no buyers"
        try:
            lowest_sell = response.json()["data"]["asks"][0]
        except IndexError:
            lowest_sell = "There are no sellers"
        print(f"{ship}, USDC: {highest_buy}")
        print(f"{ship}, USDC: {lowest_sell}")
    if len(ATLAS_adr) > 0:
        response = requests.get(url=f"{dexlab_orderbook_endpoint}/{ATLAS_adr}")
        try:
            highest_buy = response.json()["data"]["bids"][-1]
        except IndexError:
            highest_buy = "There are no buyers"
        try:
            lowest_sell = response.json()["data"]["asks"][0]
        except IndexError:
            lowest_sell = "There are no sellers"
        print(f"{ship}, ATLAS: {highest_buy}")
        print(f"{ship}, ATLAS: {lowest_sell}")
    time.sleep(0.01)


