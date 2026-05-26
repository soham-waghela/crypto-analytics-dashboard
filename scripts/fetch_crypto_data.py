import requests
import pandas as pd
import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

crypto_df = df[
    [
        "name",
        "symbol",
        "current_price",
        "market_cap"
    ]
]

crypto_df.columns = [
    "coin_name",
    "symbol",
    "current_price",
    "market_cap"
]

engine = create_engine(DATABASE_URL)

crypto_df["fetched_at"] = datetime.now()

crypto_df.to_sql(
    "crypto_prices",
    engine,
    if_exists="append",
    index=False
)


full_df = pd.read_sql(
    "SELECT * FROM crypto_prices",
    engine
)

full_df.to_csv(
    "crypto_data.csv",
    index=False
)

print("Crypto data inserted successfully!")