import os

from sec_edgar_downloader import Downloader
import requests
import pandas as pd

FILING_TYPE = '10-K'
BASE_DIR = 'Mirae_10_K_Filings'

def download_cik_list():
    headers = {'User-Agent': "x24manans@iima.ac.in"}

    # get all companies data
    company_tickers = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
    )

    companyData = pd.DataFrame.from_dict(company_tickers.json(),
                                         orient='index')

    # add leading zeros to CIK
    companyData['cik_str'] = companyData['cik_str'].astype(
        str).str.zfill(10)
    cik_list = companyData.iloc[0:5, 0].tolist()
    cik_title_list = companyData.iloc[0:5, -1].tolist()
    return cik_list, cik_title_list

def download_filing_data(cik_list, cik_title_list, filing_type, base_dir = BASE_DIR, years=1):
    for c, c_title in zip(cik_list, cik_title_list):
        download_path = os.path.join(base_dir, c_title)  # Create a unique directory for each title
        downloader = Downloader('Manan','x24manans@iima.ac.in',download_path)
        downloader.get(filing_type, c, limit=years, download_details=False)
        print(f"Downloaded filings for {c_title} at {download_path}")


def get_all_filing_paths():
    result = []

    for path, dirs, files in os.walk(BASE_DIR):
        for name in files:
            if name.lower().endswith(".txt"):
                result.append(os.path.join(path, name))

    return result
