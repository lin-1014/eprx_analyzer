import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HeatmapService } from '../../services/heatmap.service';
import * as echarts from 'echarts';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-heatmap',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.css']
})
export class HeatmapComponent implements OnInit {
  heatmapData: any; // { index: [...], columns: [...], data: [...] }
  selectedTSO: string = '中部';
  priceThreshold: number = 20;
  selectedReserveType: string = '3-2';

  constructor(private heatmapService: HeatmapService) {}

  ngOnInit(): void {
    this.heatmapService.getHeatmapData(this.selectedTSO, this.priceThreshold, this.selectedReserveType).subscribe(data => {
      this.heatmapData = data;
      this.renderHeatmap();
    });
  }

  onParameterChange(): void {
    // 當使用者在前端調整參數時，再次呼叫 API
    this.fetchAndRenderHeatmap();
  }

  fetchAndRenderHeatmap(): void {
    this.heatmapService.getHeatmapData(this.selectedTSO, this.priceThreshold, this.selectedReserveType)
      .subscribe(data => {
        this.heatmapData = data;
        this.renderHeatmap();
      });
  }

  renderHeatmap() {
    // 假設後端回傳結構為:{ index: [...], columns: [...], data: [...] }
    const chartDom = document.getElementById('heatmap-container')!;
      // 先檢查是否已有 chart Instance
    let myChart = echarts.getInstanceByDom(chartDom);
    if (!myChart) {
      // 如果還沒有，才進行初始化
      myChart = echarts.init(chartDom);
    }


    // 把 DataFrame-like 結果轉成 ECharts heatmap 需要的結構 [ [x, y, value], ... ]
    const seriesData = [];
    for (let i = 0; i < this.heatmapData.index.length; i++) {
      for (let j = 0; j < this.heatmapData.columns.length; j++) {
        seriesData.push([
          j,   // x 軸: columns (通常 weekday)
          i,   // y 軸: index (通常 block)
          this.heatmapData.data[i][j] || 0
        ]);
      }
    }

    const option = {
      tooltip: {
        position: 'top'
      },
      title: {
        text: '調整力Heatmap'
      },
      xAxis: {
        type: 'category',
        data: this.heatmapData.columns,
        splitArea: { show: true },
        name: 'Weekday'
      },
      yAxis: {
        type: 'category',
        data: this.heatmapData.index,
        splitArea: { show: true },
        name: 'Block'
      },
      visualMap: {
        min: 0,
        max: 20, // 依照資料大小調整!!!
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: '0%'
      },
      series: [{
        name: 'count',
        type: 'heatmap',
        data: seriesData,
        label: {
          show: true
        },
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }]
    };

    // 畫圖表
    myChart.setOption(option);
  }
}
