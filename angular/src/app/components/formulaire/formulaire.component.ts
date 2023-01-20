import { Component } from '@angular/core';
import { DataService } from '../../services/data.service';
import { FormGroup, FormControl, FormArray, Form } from '@angular/forms';
import * as moment from 'moment';
import { Experience } from 'src/app/model/experience/experience';
import { Technologie } from 'src/app/model/technologie/technologie';
import { Categorie } from 'src/app/model/categorie/categorie';

@Component({
  selector: 'app-formulaire',
  templateUrl: './formulaire.component.html',
  styleUrls: ['./formulaire.component.scss'],
  providers: [ DataService ]
})
export class FormulaireComponent {

  public mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
  public annees: number[] = []

  public datas: any = [];
  public categorieDatas: any = [];
  public technologieDatas: any = [];

  public formulaires: any = [];

  constructor(
    private experience: Experience,
    private technologie: Technologie,
    private categorie: Categorie,
  ) {

    for (let i = 2000; i <= 2050; i++) {
      this.annees.push(i);
    }

    this.experience.getAllExperience().subscribe((response) => {
      this.datas = response;
      this.formulaires = this.experience.datasToFormgroup(response);
    });

    this.technologie.getAllTechnologie().subscribe((response) => {
      this.technologieDatas = response;
    });

    this.categorie.getAllCategorie().subscribe((response) => {
      this.categorieDatas = response;
    });
    
  }

  public onCancel(formulaire: FormGroup) {
    let id = formulaire.get("experience_id")?.value;
    let data = this.datas.find((e: any) => e.experience_id == id);

    let technologies = data.technologies.map((e: any) => e.technologie_id);

    let remarques: any[] = [];

    data.remarques.forEach((element: any) => {
      remarques.push({
        remarque: element.remarque,
        remarque_id: element.remarque_id
      });
    });

    formulaire.patchValue({
      experience_id: data.experience_id,
      titre: data.titre,
      description: data.description,
      date_debut: data.date_debut,
      date_fin: data.date_fin,
      ordre: data.ordre,
      visible: data.visible,
      categorie_id: data.categorie_id,
      technologies_id: technologies
    });

    (formulaire.get('remarques') as FormArray).patchValue(remarques);
  }

  public onSubmit(formulaire: FormGroup) {
    let result = this.experience.formgroupToData(formulaire);
    if (typeof result.experience_id == "string") {
      this.experience.createExperience(result);
    } else {
      this.experience.updateExperience(result);
    }
  }

  public onDelete(formulaire: FormGroup, index: number) {
    this.experience.deleteExperience(formulaire);
    this.formulaires.splice(index, 1);
  }

  public addExperience() {
    //Create element and in the return get all the element and show
    this.datas.push({
      "categorie_id": 0,
      "date_debut": null,
      "date_fin": null,
      "description": "",
      "title": "",
      "experience_id": "New",
      "ordre": null,
      "remarques": [],
      "technologies": [],
      "titre": "Nouveau",
      "visible": 1
    });

    let form = new FormGroup({
      experience_id: new FormControl("New"),
      titre: new FormControl("Nouveau"),
      description: new FormControl(),
      date_debut: new FormGroup({
        date_mois: new FormControl(),
        date_annee: new FormControl(),
      }),
      date_fin: new FormGroup({
        date_mois: new FormControl(),
        date_annee: new FormControl(),
      }),
      ordre: new FormControl(),
      visible: new FormControl(),
      categorie_id: new FormControl(),
      technologies_id: new FormControl([]),
      remarques: new FormArray([])
    });

    this.formulaires.push(form);
  }
  
  public deleteRemarque(remarque: FormGroup, index: number) {
    
    let rem: any = {};
    for (const field in remarque.controls) {
      rem[field] = remarque.controls[field].value;
    }

    (remarque.parent as FormArray).removeAt(index);
  }

  public addRemarque(formulaire: FormGroup) {
    let remarque_new = new FormGroup({
      remarque_id: new FormControl("New"),
      remarque: new FormControl("Nouveau")
    });
    let remarques = formulaire.get('remarques') as FormArray;
    remarques.push(remarque_new);
  }
}
