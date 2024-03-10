import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { MonthComponent } from './home/month/month.component';
import { MovieComponent } from './home/movie/movie.component';
import { SearchComponent } from './home/search/search.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'month/:id', component: MonthComponent},
  {path: 'movie', component: MovieComponent},
  {path: 'search', component: SearchComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }
