import pandas as pd

def extract_top_stocks(number_of_stocks = 1000):
    file_path = '../data/stocks_data.csv'  # Update this path
    data = pd.read_csv(file_path)

    data['Market Cap'] = pd.to_numeric(data['Market Cap'], errors='coerce')

    top_stocks = data.sort_values(by='Market Cap', ascending=False).head(number_of_stocks)

    top_symbols = top_stocks['Symbol'].tolist()

    return top_symbols

print(extract_top_stocks())