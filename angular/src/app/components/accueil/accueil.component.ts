import { Component } from '@angular/core';
import { Categorie } from 'src/app/model/categorie/categorie';
import { Experience } from 'src/app/model/experience/experience';

@Component({
  selector: 'app-accueil',
  templateUrl: './accueil.component.html',
  styleUrls: ['./accueil.component.scss'],
})
export class AccueilComponent {
  public datas: any = {};
  public categories: any = [];

  constructor(
    private experience: Experience,
    private categorie: Categorie
  ) {

    this.categorie.getAllVisibleCategorie().subscribe((response) => {
      this.categories = response.filter((e: any) => e.visible == true);
    });

    this.experience.getAllExperience().subscribe((response) => {
      this.categories.forEach((categorie: any) => {
        this.datas[categorie.titre] = response.filter((e: any) => categorie.categorie_id == e.categorie_id)
      });
    });

  }
}
