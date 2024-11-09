from lib.util import *

cik_list, cik_title = download_cik_list()
download_filing_data(cik_list, cik_title, FILING_TYPE, years = 2)
file_path_list = get_all_filing_paths()

