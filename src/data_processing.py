import logging
import zipfile

from pandas import concat, read_csv, to_datetime

from utils.logger import setup_logging

setup_logging()


def load_eprx_data():
    """
    _summary_
    """
    df_list = []
    # set ZIP file path
    zip_file_path = r"raw_data/2024_3-2_result.zip"

    if not zipfile.is_zipfile(zip_file_path):
        raise FileNotFoundError(f"{zip_file_path} is not a valid ZIP file.")

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            with zip_ref.open(filename) as file:
                lines = []
                for _ in range(2):
                    lines.append(file.readline().decode("cp932").strip())
                # header_info_1, header_info_2 = lines[0], lines[1]
                # print(f"Header 1: {header_info_1}",
                #       f"Header 2: {header_info_2}")
                per_month_df = read_csv(file, encoding="cp932",)

                if per_month_df.iloc[-1].notna().sum() == 1 and per_month_df.iloc[-1].fillna('').str.contains('^E$').any():
                    # 最後一行可能會是E
                    per_month_df = per_month_df.drop(
                        per_month_df.tail(1).index)
                df_list.append(per_month_df)
                logging.info("Loaded %d rows from ZIP file.", len(per_month_df))

    merged_df = concat(df_list, ignore_index=True)
    return merged_df


def filter_eprx_dataframe(eprx_df, wanted_col, filter_condition):
    """
    根據指定欄位和篩選條件篩選 DataFrame。

    Parameters:
    - df (DataFrame): 原始 DataFrame
    - wanted_col (list): 要保留的欄位名稱
    - filter_condition (dict): 篩選條件，鍵為欄位名稱，值為要篩選的值

    Returns:
    - pd.DataFrame: 篩選後的 DataFrame。
    """
    # 篩選指定Column
    df_filtered = eprx_df[wanted_col]

    # 根據條件篩選列row
    for column, value in filter_condition.items():
        df_filtered = df_filtered[df_filtered[column] == value]

    return df_filtered


def extract_date_block_info(df, tt_column='TT'):
    """
    從指定的 TT 欄位提取日期、區塊和星期。

    Parameters:
    - df (DataFrame): 要處理的 DataFrame。
    - tt_column (str): 包含 TT 資料的欄位名稱，預設 'TT'。

    Returns:
    - pd.DataFrame: 新增欄位後的 DataFrame。
    """
    df['Block'] = df[tt_column].str[-3:]
    df['Date'] = to_datetime(df[tt_column].str[:8], format='%Y%m%d')
    df['Weekday'] = df['Date'].dt.weekday
    return df
