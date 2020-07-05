import pandas as pd
from os import walk

def run_job():
    path = '/home/omar/Downloads/x/dim_products_tracked/Original/date='

    date_list = pd.date_range(start="2020-05-31",end="2020-06-24").format()
    for date in date_list:
        files = []
        for (dirpath, dirnames, filenames) in walk(path + date + '/'):
            files.extend(filenames)
            break

        all_dfs = pd.DataFrame()
        for f in files:
            print(f'Reading {f}')
            df = pd.read_parquet(path + date + '/' + f)
            if (all_dfs.empty):
                all_dfs = df
            else:
                all_dfs = all_dfs.append(df)
            print(f'{f} appended to pqt file\n')

        all_dfs.to_parquet('./reports/' + 'x-' + date + '.parquet')
    # logger.info("finished writing parquet")


if __name__ == "__main__":
    try:
        run_job()
    except Exception as e:
        raise
