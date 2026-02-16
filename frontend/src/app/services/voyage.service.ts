import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';
import { inject } from '@angular/core';
import { environment } from '../../environments/environment';

export interface Voyage {
  id?: number;
  ship: number;
  ship_name?: string;
  start_port: string;
  destination_port: string;
  start_date: string;
  end_date: string;
  created_at?: string;
  updated_at?: string;
}

@Injectable({
  providedIn: 'root'
})
export class VoyageService {
  private apiUrl = `${environment}.apiUrl/voyages`;
  private http = inject(HttpClient);

  getVoyages(): Observable<Voyage[]> {
    return this.http.get<Voyage[]>(this.apiUrl);
  }
}
