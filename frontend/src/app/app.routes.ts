import { Routes } from '@angular/router';
import { ShipListComponent} from "./components/ship-list/ship-list.component";

export const routes: Routes = [
  { path: 'ships', component: ShipListComponent },
  { path: '', redirectTo: '/ships', pathMatch: 'full' }
];
