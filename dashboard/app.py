import streamlit as st
import pandas as pd
import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide"
)

st_autorefresh(interval=60000, key="refresh")
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)

# query = "SELECT * FROM crypto_prices"

# df = pd.read_sql(query, engine)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(BASE_DIR, "crypto_data.csv")
df = pd.read_csv(csv_path)

selected_coins = st.sidebar.multiselect(
    "Select Cryptocurrencies",
    df["coin_name"].unique(),
    default=df["coin_name"].unique()
)

filtered_df = df[df["coin_name"].isin(selected_coins)]

filtered_df["fetched_at"] = pd.to_datetime(
    filtered_df["fetched_at"]
)

latest_df = (
    filtered_df
    .sort_values("fetched_at")
    .drop_duplicates(
        subset="coin_name",
        keep="last"
    )
)

st.title("Crypto Analytics Dashboard")

st.write("Live Cryptocurrency Market Data")

if not filtered_df.empty:
  
    total_market_cap = latest_df["market_cap"].sum()

    average_price = latest_df["current_price"].mean()

    largest_crypto = latest_df.loc[
        latest_df["market_cap"].idxmax(),
        "coin_name"
    ]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Market Cap",
        f"${total_market_cap:,.0f}"
    )

    col2.metric(
        "Average Price",
        f"${average_price:,.2f}"
    )

    col3.metric(
        "Largest Cryptocurrency",
        largest_crypto
    )

    st.dataframe(
    latest_df.sort_values(
        by="market_cap",
        ascending=False)
    )

    st.subheader("Cryptocurrency Prices")

    st.bar_chart(
    latest_df.set_index("coin_name")["current_price"]
    )

    st.subheader("Market Share Distribution")

    market_share_df = latest_df.set_index(
    "coin_name"
    )["market_cap"]

    fig = market_share_df.plot.pie(
        autopct='%1.1f%%',
        figsize=(8,8)
    ).figure

    st.pyplot(fig)

    st.subheader("Top Cryptocurrencies")

    top_coins = latest_df.sort_values(
    by="market_cap",
    ascending=False
    )

    st.dataframe(
        top_coins[
            ["coin_name", "current_price", "market_cap"]
        ]
    )

    st.subheader('Histrorical Price Trends')

    historical_prices = filtered_df.sort_values(
    by="fetched_at"
    )

    historical_prices["fetched_at"] = pd.to_datetime(
    historical_prices["fetched_at"]
    )

    historical_prices["formatted_time"] = (
    historical_prices["fetched_at"]
    .dt.strftime("%H:%M")
    )

    pivot_df = historical_prices.pivot_table(
    index="formatted_time",
    columns="coin_name",
    values="current_price"
    )
    st.line_chart(pivot_df)


    returns_df = pivot_df.pct_change()*100
    st.subheader("Cryptocurrency Returns")
    st.line_chart(returns_df)  

    st.subheader('Volatility Analysis')
    volatility_df = returns_df.std().sort_values(ascending=False)
    st.bar_chart(volatility_df)

    st.subheader('Correlation Matrix')
    correlation_df = returns_df.corr()
    st.dataframe(correlation_df)

else:
  st.warning("No cryptocurrencies selected. Please select at least one cryptocurrency from the sidebar.")
