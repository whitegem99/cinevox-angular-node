import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { MoviesService } from '../core/service/movies.service';
import { NgOptimizedImage } from '@angular/common'

@Component({
  providers: [AppComponent ],
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent{

  constructor(
    private app: AppComponent
  ) {}

  public languages = [
    "EN",
    "FR",
    "NL"
  ]
  public local = 'EN'

  public changeLocal(language: string){
    this.local = language

    this.app.changeLanguage(language.toLowerCase())
  }
}
