import pandas as pd
import asyncio
import cybotrade_datasource
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('CYBOTRADE_API_KEY')

'''
async def main():
    data = await cybotrade_datasource.query_paginated(
        api_key=API_KEY, 
        topic='cryptoquant|btc/inter-entity-flows/miner-to-miner?from_miner=f2pool&to_miner=all_miner&window=hour', 
        start_time=datetime(year=2024, month=1, day=1, tzinfo=timezone.utc),
        end_time=datetime(year=2025, month=1, day=1, tzinfo=timezone.utc)
    )
    df = pd.DataFrame(data)
    print(df)
    

asyncio.run(main())
'''

'''
async def main():
    stream = await cybotrade_datasource.stream(
        api_key=API_KEY,
        topics=[
            'cryptoquant|btc/inter-entity-flows/miner-to-miner?from_miner=f2pool&to_miner=all_miner&window=hour',
            'cryptoquant|btc/market-data/liquidations?exchange=deribit&window=min',
        ],
    )
    async for msg in stream:
        print(msg)
    

asyncio.run(main())
'''

async def get_data(topic):
    data = await cybotrade_datasource.query_paginated(
        api_key=API_KEY, 
        topic=topic, 
        limit=10000
    )
    return pd.DataFrame(data)


async def main():
    topics = [
        'cryptoquant|btc/inter-entity-flows/miner-to-miner?from_miner=f2pool&to_miner=all_miner&window=hour',
        'cryptoquant|btc/exchange-flows/inflow?exchange=okx&window=hour',
        'glassnode|blockchain/utxo_created_value_median?a=BTC&c=usd&i=1h',
    ]

    tasks = [get_data(topic) for topic in topics]
    dataframes = await asyncio.gather(*tasks)

    for i, df in enumerate(dataframes):
        print(f"DataFrame {i+1} ({topics[i]})")
        print(df.head)

asyncio.run(main())
