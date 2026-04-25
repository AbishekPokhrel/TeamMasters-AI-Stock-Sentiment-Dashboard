import yfinance as yf
import pandas as pd


def get_company_name(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return info.get("longName") or info.get("shortName") or ticker.upper()
    except Exception:
        return ticker.upper()


def get_stock_data(ticker, period="1mo"):
    try:
        df = yf.download(ticker, period=period, progress=False)
        if df is None or df.empty:
            return pd.DataFrame()
        return df
    except Exception:
        return pd.DataFrame()