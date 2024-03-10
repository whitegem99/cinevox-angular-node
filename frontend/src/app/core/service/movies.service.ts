import { Injectable, OnInit } from '@angular/core';
import { Movie } from '../model/movie';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {

    public movies!: Movie[];
    
    constructor(private http: HttpClient){
    }
    
    async getAllMovies(): Promise<Movie[]>{
      const baseUrl = environment.apiUrl

      var movies = await firstValueFrom(this.http.get<Array<Movie>>(baseUrl + "/api/movies"))
   
      return this.sortMovies(movies)
    }

    private sortMovies(movies: Movie[]): Movie[]{
      const d = new Date();
      let currentMonth = d.getMonth();
      console.log(d)
      console.log(currentMonth)
      var sortedMovies = []
      
      for (var month = currentMonth; month < 12 + currentMonth; month++){
        sortedMovies[month%12] = movies[month]
      }

      return sortedMovies
    }
}
