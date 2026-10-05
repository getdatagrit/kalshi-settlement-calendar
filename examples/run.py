# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/kalshi-settlement-calendar").call(run_input={
    "settlesWithinHours": 48,
    "maxItems": 50
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
