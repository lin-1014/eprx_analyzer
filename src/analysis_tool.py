from pandas import crosstab
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams



def analyze_and_visualize_heatmap(
    df,
    value_column,
    filter_value,
    group_columns,
    return_count=False
):
    """
    根據欄位篩選資料並計算分組次數，根據參數選擇返回分組次數或繪製熱力圖。

    Parameters:
    - df (DataFrame): 原始資料 DataFrame。
    - value_column (str): 用於篩選的欄位名稱（如 '中部'，代表中部電力市場的價格）。
    - filter_value (float): 篩選的TSO結清價錢閥值（如 > 20）。
    - group_columns (list): 分組欄位名稱（如 ['Block', 'Weekday']）。
    - return_count (bool): 如果為 True，返回分組次數（不繪製圖表）。

    Returns:
    - 如果 return_count=True，返回分組次數的 Series。
    - 如果 return_count=False，繪製熱力圖（不返回值）。
    """
    # 設定字型（確保支援日文）
    rcParams['font.family'] = 'SimSun'

    # 篩選資料
    filtered_df = df[df[value_column] > filter_value]

    # 計算分組次數
    count_distribution = filtered_df.groupby(group_columns).size()

    if return_count:
        # 返回分組次數
        return count_distribution
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
