from email.header import Header

import pandas as pd

def extract_top_stocks(number_of_stocks = 1000):
    file_path = '../data/stocks_data.csv'  # Update this path
    data = pd.read_csv(file_path)

    data['Market Cap'] = pd.to_numeric(data['Market Cap'], errors='coerce')

    top_stocks = data.sort_values(by='Market Cap', ascending=False).head(number_of_stocks)

    top_symbols = top_stocks['Symbol'].tolist()

    return top_symbols


def get_cik_list_from_tickers(tickers):
    ciksDF = pd.read_csv('../data/sym_to_cik.csv', header=None)
    ciksDF = ciksDF.set_index(0)
    cik_list = []
    for ticker in tickers:
        try:
            cik_list.append(int(ciksDF.loc[ticker.lower(), 1]))
        except:
            print("CIK not found for {}".format(ticker))
    return cik_list

print(get_cik_list_from_tickers(extract_top_stocks()))
