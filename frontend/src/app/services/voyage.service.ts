import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from "../../environments/environment";

export interface Voyage {
  id?: number;
  ship: number;
  ship_details?: string;
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
  private apiUrl = `${environment.apiUrl}voyages/`;
  private http = inject(HttpClient);

  getVoyages(): Observable<VoyageService[]> {
    return this.http.get<VoyageService[]>(this.apiUrl)
  }

  getVoyage(id: number): Observable<VoyageService> {
    return this.http.get<VoyageService>(`${this.apiUrl}${id}/`);
  }
}
