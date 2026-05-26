import pandas as pd
import matplotlib.pyplot as plt
import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM crypto_prices"

df = pd.read_sql(query, engine)

# print(df.info())
# print(df.describe())

top_market_cap = df.sort_values(by="market_cap",ascending=False)

print(top_market_cap[["coin_name","market_cap"]])

df["market_share"] = (df["market_cap"] /df["market_cap"].sum()) * 100

print(df[["coin_name", "market_share"]])

plt.figure(figsize=(12, 6))

plt.bar(
    df["coin_name"],
    df["current_price"]
)

plt.title("Cryptocurrency Prices")
plt.xlabel("Cryptocurrency")
plt.ylabel("Current Price (USD)")
plt.xticks(rotation=45)
plt.savefig("images/crypto_prices.png")
plt.show()