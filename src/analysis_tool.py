from pandas import crosstab
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams



def analyze_and_visualize_heatmap(
    df,
    value_column,
    filter_value,
    group_columns,
    return_data=False
):
    """
    根據欄位篩選資料並計算分組次數，根據參數選擇返回分組次數或繪製熱力圖。

    Parameters:
    - df (DataFrame): 原始資料 DataFrame。
    - value_column (str): 用於篩選的欄位名稱（如 '中部'，代表中部電力市場的價格）。
    - filter_value (float): 篩選的TSO結清價錢閥值（如 > 20）。
    - group_columns (list): 分組欄位名稱（如 ['Block', 'Weekday']）。
    - return_data (bool): 如果為 True，返回分組次數（不繪製圖表）。

    Returns:
    - 如果 return_data=True，返回分組次數的 Series。
    - 如果 return_data=False，繪製熱力圖（不返回值）。
    """
    # 設定字型（確保支援日文）
    rcParams['font.family'] = 'SimSun'

    # 篩選資料
    filtered_df = df[df[value_column] > filter_value]

    # 製作交叉表
    heatmap_data = crosstab(filtered_df[group_columns[0]], filtered_df[group_columns[1]])
    # 避免數值小於filter被篩除掉的問題(有些區塊在某些星期沒有資料)
    all_blocks = df[group_columns[0]].unique()
    heatmap_data = heatmap_data.reindex(all_blocks, fill_value=0)
    all_weekdays = df[group_columns[1]].unique()
    heatmap_data = heatmap_data.reindex(index=all_blocks, columns=all_weekdays, fill_value=0)

    if return_data:
        result = heatmap_data.to_dict(orient="split")
        return result
    else:
        # 製作交叉表
        heatmap_data = crosstab(filtered_df[group_columns[0]], filtered_df[group_columns[1]])

        # 繪製熱力圖
        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', cbar=True)
        plt.title(f'{value_column} & over {filter_value} yen {group_columns[0]} and {group_columns[1]} Count Heatmap (24/04 to 24/11)')
        plt.xlabel(f'{group_columns[1]} (0=Monday, 6=Sunday)')
        plt.ylabel(group_columns[0])
        plt.show()
