import argparse

from bs4 import BeautifulSoup
import os
import pandas as pd
import requests
import shutil

# default write parameters
OUTPUT_DIR_PATH = '.'
OUTPUT_DIR_NAME = 'html2csv_output'

def make_output_dir(return_dir=False, overwrite=False):
    output_dir = os.path.join(f'{OUTPUT_DIR_PATH}', f'{OUTPUT_DIR_NAME}')
    dir_exists = os.path.isdir(output_dir)
    
    if dir_exists:
        if overwrite == True:
            print(f'Deleting the directory {output_dir} ...')
            shutil.rmtree(output_dir)
            print(f'Done.\n')

            print(f'Creating output directory at {output_dir} ...')
            os.mkdir(output_dir)
            print('Done.\n')
        else:
            print(f'The directory {output_dir} already exists. To overwrite the directory set `overwrite=False`.')
    else:
        print(f'Creating output directory at {output_dir} ...')
        os.mkdir(output_dir)
        print('Done.')
        
    # return dir name if `return_dir=True`
    if return_dir:
        return output_dir
    
def pandas_html2csv(url, write=True):
    dfs = pd.read_html(url)
    if write == True:
        output_dir = make_output_dir(return_dir=True, overwrite=True)
        for i, df in enumerate(dfs):
            fn = f'html2csv_pandas_{i}.csv'
            fp = os.path.join(output_dir, fn)
            df.to_csv(fp)
            print(f'Wrote table to csv: {fp}')
        print('Done.')
    else:
        print(*dfs)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(
		description='Download csvs from html tables from webpage url.'
	)
	parser.add_argument(
		'url', 
		type=str, 
		nargs=1, 
		help='url of webpage'
	)
	args = parser.parse_args()
	url = args.url[0]
	pandas_html2csv(url, write=True)