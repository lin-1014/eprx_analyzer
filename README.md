# Market Analysis for Demand and Supply Adjustment (需給調整市場)

- Specialized in analyzing the design of Japan's demand and supply adjustment market, assisting energy storage systems to participate in the tertiary adjustment capacity② (3-2) market by providing bidding strategy analysis.

### Background
The Japanese tertiary adjustment capacity② market adopts a multi-price auction design where bidding decisions do not consider generator prices. This has led many energy storage systems to miss out due to low maximum clearing prices (e.g., 0.5 yen). By analyzing the "highest clearing price" in the market data, this project helps users set a price threshold (e.g., above 30 yen) to investigate the frequency and distribution of high prices in each area (TSO). It then provides optimal bidding strategies based on historical data from April to November.

### Expected Functions

1. **Data Processing & Filtering**  
   - Decompress and load the market data provided by EPRX.  
   - Filter data based on specified conditions (e.g., price thresholds).  

2. **Heatmap Visualization**  
   - Generate a Block × Weekday heatmap showing the frequency of high-price occurrences, based on the defined price threshold and TSO (electric power company).

3. **Strategy Recommendations**  
   - Analyze historical data to identify the combination of Blocks and weekdays with the highest likelihood of successful bids.

### Usage Instructions

1. **Installation**  
   Ensure Python 3.8+ and poetry are installed, then run one of the following commands to install required packages:
   ```bash
   poetry install
   # or (tentative)
   pip install -r requirements.txt

2. **Data Preparation**
Place the target EPRX ZIP file into the raw_data/ folder. For example:

```
raw_data/2024_3-2_result.zip
```

3. **Running the Analysis**
In the terminal, execute:
```bash
python main.py
```
4. **Parameter Configuration**
In main.py, you can modify these parameters:

target_tso: The target electric power company (e.g., Chubu, Tohoku).
price_threshold: The price threshold (e.g., 25 or 30 yen).

### Results & Examples

1. High-Price Frequency Heatmap
A heatmap visualizing how often high prices appear for each Block and weekday helps estimate bidding success.

2. Recommended Strategy:

Weekday X × Block X (XX:00-XX:00)
Weekday X × Block 6 (15:00-18:00)
Example Heatmap

![local image][def]


[def]: ./docs/images/tokyo_example.png


# 需給調整市場分析(中文版本)

- 專門分析日本需給調整市場設計，協助儲能系統參與三次調整力②市場的投標策略分析。

## 背景

日本三次調整力②市場採用複數價格標（Multi-Price Auction），且投標決策不考慮機組價格，導致許多儲能系統因最高結清價格偏低（如 0.5 日元）無法得標。本專案通過分析市場資料中 "最高結清價格"，協助使用者設定價格門檻（如超過 30 日元），以研究各區域（TSO）中高價出現的次數及分布，並根據 4 至 11 月的歷史資料提供最佳投標策略。

---

## 預計功能

1. **資料處理與篩選**：
   - 解壓並載入 EPRX 提供的市場資料。
   - 篩選指定條件（如價格門檻）的數據。

2. **熱力圖可視化**：
   - 根據設定的價格門檻和電力公司別（TSO），生成高價出現次數的 Block × Weekday 熱力圖。

3. **策略建議**：
   - 分析歷史數據，找出得標機率最高的 Block 和星期組合。

---

## 使用方式

1. 安裝依賴
請確保你已安裝 Python 3.8+與poetry套件，並使用以下命令安裝所需套件：

```python
poetry install
或(暫定)
pip install -r requirements.txt
```

2. 資料準備
將目標 EPRX ZIP 檔案放置於 raw_data/ 資料夾下。例如：

```
raw_data/2024_3-2_result.zip
```
3. 執行分析
在終端執行以下命令：

```bash
python main.py
```
4. 參數設置
在 main.py 中，可修改以下參數進行自定義：
    - target_tso：目標電力公司（例如：中部、東北）。
    - price_threshold：價格門檻（例如：25 或 30 日元）。

## 結果與示例

1. 高價次數熱力圖： 熱力圖顯示各 Block 與星期的高價出現次數分布，幫助了解得標可能性。

策略建議：

可優先考慮：
星期X × Block X（XX:00-XX:00）
星期X × Block 6（15:00-18:00）

2. 範例熱力圖
![本地圖片][def]


[def]: ./docs/images/tokyo_example.png