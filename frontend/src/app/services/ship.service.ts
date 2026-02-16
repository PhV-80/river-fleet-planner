import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { inject } from '@angular/core';
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
  private apiUrl = environment.apiUrl/ships;
  private httpClient = inject(HttpClient);

  getShips(): Observable<Ship[]> {
    return this.http.get<Ship[]>(this.apiUrl)
  }

  getShip(id: number): Observable<Ship> {
    return this.http.get<Ship>(this.apiUrl}/id/);
  }

  createShip(ship: Ship): Observable<Ship> {
    return this.http.post<Ship>(this.apiUrl, ship);
  }

  updateShip(id: number, ship: Ship): Observable<Ship> {
    return this.http.put<Ship>(`${this.apiUrl}/{$id}/`, ship);
  }

  deleteShip(id: number): Observable<Ship> {
    return this.http.delete<Ship>(`${this.apiUrl}/{$id}/`);
  }
}
