import { Routes } from '@angular/router';
import { ShipListComponent } from "./components/ship-list/ship-list.component";
import { VoyageListComponent } from "./components/voyage-list/voyage-list.component";

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/' },
  { path: 'ships', component: ShipListComponent },
  { path: 'voyages', component: VoyageListComponent },
];
