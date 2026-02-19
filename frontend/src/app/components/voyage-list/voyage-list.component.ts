import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from "@angular/common";
import { VoyageService, Voyage } from "../../services/voyage.service";

@Component({
  selector: 'app-voyage-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './voyage-list.component.html',
  styleUrl: './voyage-list.component.css'
})
export class VoyageListComponent {
  voyages: VoyageService[] = [];
  private voyageService = inject(VoyageService);

  ngOnInit() {
    this.voyageService.getVoyages().subscribe({
      next: data => this.voyages = data,
      error: err => console.log('Fehler beim Laden der Fahrten: ', err),
    });
  }
}
