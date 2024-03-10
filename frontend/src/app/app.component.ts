import { Component, OnInit } from '@angular/core';
import { MoviesService } from './core/service/movies.service';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  title = 'belgotheque';
  movies!: any[];
  moviesSet = false

  constructor(
    private moviesService: MoviesService,
    private translate: TranslateService
  ) {}

  async initMovies(): Promise<void>{
    this.movies = await this.moviesService.getAllMovies()
    this.moviesSet = true
  }

  currentLanguage: string = 'en'

  changeLanguage(newLanguage : string): void {
    this.translate.use(newLanguage)
    this.currentLanguage = newLanguage
  }

}
