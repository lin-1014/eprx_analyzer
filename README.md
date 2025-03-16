# Market Analysis for Demand and Supply Adjustment (需給調整市場)

- Specialized in analyzing the design of Japan's demand and supply adjustment market, assisting energy storage systems to participate in the tertiary adjustment capacity② (3-2) market by providing bidding strategy analysis.

- This project has been upgraded to a web-based interface for analyzing Japan’s demand and supply adjustment market. Users can select the region (TSO), reserve type, and price threshold, and the system will automatically generate a heatmap of high-price occurrences.

- Online Demo: https://arctic-depth-433311-e0.an.r.appspot.com/

### Background
The Japanese tertiary adjustment capacity② market adopts a multi-price auction design where bidding decisions do not consider generator prices. This has led many energy storage systems to miss out due to low maximum clearing prices (e.g., 0.5 yen). By analyzing the "highest clearing price" in the market data, this project helps users set a price threshold (e.g., above 30 yen) to investigate the frequency and distribution of high prices in each area (TSO). It then provides optimal bidding strategies based on historical data from Jan to Dec of 2024.

---
### Features

1. **Data Processing & Filtering**  
   - Loads and decompresses EPRX market data.
   - Filters data based on specified criteria (e.g., price threshold).

2. **Heatmap Visualization**  
   - Generate a Block × Weekday heatmap showing the frequency of high-price occurrences, based on the defined price threshold and TSO (electric power company).

3. **Strategy Recommendations (TODO)**  
   - Analyze historical data to identify the combination of Blocks and weekdays with the highest likelihood of successful bids.
---

### Usage

1. Visit  https://arctic-depth-433311-e0.an.r.appspot.com/
2. Select the parameters:
   - Reserve Type (調整力別)(例如：一次調整力、三次調整力①、三次調整力②)
   - TSO (TSO別)(例如：中部、北海道、東北、東京、北陸、關西、中國、四國、九州)
   - Threshold (yen) (しきい値(円))(例如：25 或 30)
3. The heatmap is generated automatically, showing how frequently each weekday and block exceeds your threshold.
4. Use the heatmap to identify optimal weekday-block combinations for bidding.


### Results & Examples

1. High-Price Frequency Heatmap
A heatmap visualizing how often high prices appear for each Block and weekday helps estimate bidding success.

2. Recommended Strategy:

Weekday X × Block X (XX:00-XX:00)
Weekday X × Block 6 (15:00-18:00)
Example Heatmap

![local image][def]


[def]: ./docs/images/tokyo_example.png



### Disclaimer

The data used in this project comes from the Electricity Power Resource Exchange (EPRX) website: [https://www.eprx.or.jp/](https://www.eprx.or.jp/).  
The content provided by EPRX is publicly available and free to use, provided that proper attribution to EPRX is included. If any modifications or edits are made to the content, a note indicating the modifications must be included as well.  
EPRX assumes no responsibility for any actions, analyses, or conclusions drawn from the data provided. Users are advised to exercise discretion and responsibility when using this information.

---

# 需給調整市場分析(中文版本)

- 此專案已更新為網頁化介面，提供互動式的日本需給調整市場分析。使用者可直接選擇地區 (TSO)、調整力別，以及價格門檻後，即可自動產生對應的高價頻度熱力圖。

- 線上示範： https://arctic-depth-433311-e0.an.r.appspot.com/


## 背景

日本三次調整力②市場採用複數價格標（Multi-Price Auction），且投標決策不考慮機組價格，導致許多儲能系統因最高結清價格偏低（如 0.5 日元）無法得標。本專案通過分析市場資料中 "最高結清價格"，協助使用者設定價格門檻（如超過 30 日元），以研究各區域（TSO）中高價出現的次數及分布，並根據 2024年 1 至 12 月的歷史資料提供最佳投標策略。

---

## 功能簡介

1. **資料過濾與分析**：
   - 解壓並載入 EPRX 提供的市場資料。
   - 篩選指定條件（如價格門檻）的數據。

2. **互動式熱力圖**：
   - 根據設定的價格門檻和電力公司別（TSO），產生高價出現次數的 Block × Weekday 熱力圖。

3. **策略建議(未來)**：
   - 根據歷史數據，協助找出高價出現頻率較高之星期與時段（Block），輔助儲能系統參與三次調整力市場之投標決策。

---

## 使用方式

1. 前往 https://arctic-depth-433311-e0.an.r.appspot.com/

2. 在頁面中選擇：
   - 調整力別（例如：一次調整力、三次調整力①、三次調整力②）
   - TSO別（例如：中部、北海道、東北、東京、北陸、關西、中國、四國、九州）
   - しきい値（円）（例如：25 或 30）
3. 完成設定後，系統會自動產生對應的熱力圖，顯示高價出現的頻率分布。
4. 參考熱力圖結果，即可判斷哪個星期及時段最常出現高於門檻的價格，做為投標策略參考。

## 結果與示例

1. 高價次數熱力圖： 熱力圖顯示各 Block 與星期的高價出現次數分布，幫助了解得標可能性。

策略建議：

可優先考慮：
星期X × Block X（XX:00-XX:00）
星期X × Block 6（15:00-18:00）

2. 範例熱力圖
![本地圖片][def]


[def]: ./docs/images/tokyo_example.png


### Disclaimer

使用的資料來自電力需給調整力交易所（EPRX）網站：[https://www.eprx.or.jp/](https://www.eprx.or.jp/)。  
EPRX 提供的內容可自由使用，但需正確標明出處。如果對內容進行了修改或加工，必須在使用時附加修改說明。  
請注意，EPRX 不對使用者基於此數據進行的行為、分析或結論負責。用戶在使用相關信息時應謹慎並承擔責任。
