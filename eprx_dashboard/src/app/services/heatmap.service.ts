// heatmap.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HeatmapService {
  private apiUrl = 'http://127.0.0.1:8000/heatmap/';
  constructor(private http: HttpClient) { }

  getHeatmapData(targetTso: string, threshold: number, targetReserveType: string): Observable<any> {

    const params = { target_tso: targetTso, price_threshold: threshold , target_reserve_type: targetReserveType};
    return this.http.get(this.apiUrl, { params });
  }
}
