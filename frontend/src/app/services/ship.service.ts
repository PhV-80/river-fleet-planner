import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export interface Ship {
  id?: number;
  name: string;
  capacity: number;
  status: 'available' | 'in_voyage' | 'maintenance';
  created_at?: string;
  updated_at?: string;
}

@Injectable({
  providedIn: 'root'
})
export class ShipService {
  private apiUrl = `${environment.apiUrl}ships/`;
  private http = inject(HttpClient);

  getShips(): Observable<Ship[]> {
    return this.http.get<Ship[]>(this.apiUrl);
  }

  getShip(id: number): Observable<Ship> {
    return this.http.get<Ship>(`${this.apiUrl}${id}/`);
  }
}
