import yfinance as yf

def fetch_appl_data(ticker, period = '5y'):
    #Fetch the historical stock data for appl
    stock_data = yf.Ticker(ticker).history(period = period)
    #Save this data to a csv in the data directory
    stock_data.to_csv(f"../data/{ticker}_data.csv")
    print(f"Data for {ticker} saved.")

if __name__ == '__main__':
    fetch_appl_data('AAPL')