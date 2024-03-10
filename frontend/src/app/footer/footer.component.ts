import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { MoviesService } from '../core/service/movies.service' 
import { HeaderComponent } from '../header/header.component'

@Component({
  providers: [AppComponent ],
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  constructor(
    private app: AppComponent
  ) {}

  allMonths: any = []

  async ngOnInit(): Promise<void> {
    const d = new Date();
    let currentMonth = d.getMonth();

    for (var month = currentMonth; month < 12 + currentMonth; month++){
      this.allMonths.push(month%12)
    }
  }

  public getCurrentLanguage(): string {
    return this.app.currentLanguage
  }

  public getMonthNameLong(month: number){
    const date = new Date();
    date.setMonth(month);

    const currentLanguage = this.getCurrentLanguage()
    var languageFormat
    if (currentLanguage == "fr"){
      languageFormat = "fr-BE"
    } else if (currentLanguage == "en"){
      languageFormat = 'en-US'
    } else {
      languageFormat = "nl-BE"
    }

    return date.toLocaleString(languageFormat, { month: 'long' });
  }

  public getMonthNameShort(month: number){
    const monthLong = this.getMonthNameLong(month)

    return monthLong.substring(0, 3);
  }
}
