// heatmap.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class HeatmapService {
  private apiUrl = environment.apiUrl;
  constructor(private http: HttpClient) { }

  getHeatmapData(targetTso: string, threshold: number, targetReserveType: string): Observable<any> {

    const params = { target_tso: targetTso, price_threshold: threshold , target_reserve_type: targetReserveType};
    return this.http.get(`${this.apiUrl}/heatmap/`, { params });
  }
}
