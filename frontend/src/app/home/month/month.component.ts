import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { MoviesService } from '../../core/service/movies.service'
import { Movie } from '../../core/model/movie';


@Component({
  selector: 'app-month',
  templateUrl: './month.component.html',
  styleUrls: ['./month.component.scss']
})
export class MonthComponent implements OnInit{
  id: string | null | undefined;

  constructor(
    private route: ActivatedRoute,
    private movieService: MoviesService  
  ) {}
  
  public movies!: Movie[]

  async ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id')
    const data = await this.movieService.getAllMovies()
    this.movies = data
  }

  displayMovies(){
    console.log(this.movies)
  }

}
