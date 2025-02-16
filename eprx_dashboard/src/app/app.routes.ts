import { Routes } from '@angular/router';
import { HeatmapComponent } from './pages/heatmap/heatmap.component';

export const routes: Routes = [
    { path: 'heatmap', component: HeatmapComponent },
    { path: '', component: HeatmapComponent },

];
