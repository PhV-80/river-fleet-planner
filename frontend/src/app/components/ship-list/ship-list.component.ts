import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShipService, Ship } from "../../services/ship.service";

@Component({
  selector: 'app-ship-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ship-list.component.html',
  styleUrl: './ship-list.component.css'
})
export class ShipListComponent {
  ships: Ship[] = [];
  private shipService = inject(ShipService);

  ngOnInit() {
    this.shipService.getShips().subscribe({
      next: data => this.ships = data,
      error: err => console.log('Fehler beim Laden der Schiffe:', err),
    });
  }
}
