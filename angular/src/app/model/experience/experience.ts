import { Injectable } from "@angular/core";
import { FormArray, FormControl, FormGroup } from "@angular/forms";
import { Observable, Subject } from "rxjs";
import { DataService } from "src/app/services/data.service";

@Injectable({
  providedIn: 'root'
})
export class Experience {
  public datas: any = [];

  constructor(private dataService: DataService) {

  }

  public getAllExperience() : Observable<any> {
    var subject = new Subject<any>();
    let url = "http://127.0.0.1:5000/experience"
    let data = this.dataService.getData(url);
    data.subscribe((response) => {
      this.datas = response;
      subject.next(this.datas);
    });
    return subject.asObservable();
  }

  public datasToFormgroup(datas: any[]) {
    let formulaires: any[] = []
    this.datas.forEach((element: any) => {

      let technologies = element.technologies.map((e: any) => e.technologie_id);

      let remarques: any[] = [];

      element.remarques.forEach((element: any) => {
        remarques.push(new FormGroup({
          remarque: new FormControl(element.remarque),
          remarque_id: new FormControl(element.remarque_id)
        }));
      });

      let remarquesFormArray = new FormArray(remarques);

      let form = new FormGroup({
        experience_id: new FormControl(element.experience_id),
        titre: new FormControl(element.titre),
        description: new FormControl(element.description),
        date_debut: new FormGroup({
          date_mois: new FormControl(element.date_debut ? new Date(element.date_debut).getMonth() : null),
          date_annee: new FormControl(element.date_debut ? new Date(element.date_debut).getFullYear() : null)
        }),
        date_fin: new FormGroup({
          date_mois: new FormControl(element.date_fin ? new Date(element.date_fin).getMonth() : null),
          date_annee: new FormControl(element.date_fin ? new Date(element.date_fin).getFullYear() : null)
        }),
        ordre: new FormControl(element.ordre),
        visible: new FormControl(element.visible),
        categorie_id: new FormControl(element.categorie_id),
        technologies_id: new FormControl(technologies),
        remarques: remarquesFormArray
      });

      formulaires.push(form);
    });
    return formulaires;
  }

  public formgroupToData(formulaire: FormGroup) {
    let result: any = {};
    let id = formulaire.get("experience_id")?.value;
    let data = this.datas.find((e: any) => e.experience_id == id);

    let technos_old_id = data.technologies.map((e: any) => e.technologie_id);
    let remarques_old = data.remarques;
    let remarques_old_id = data.remarques.map((e: any) => e.remarque_id);

    for (const field in formulaire.controls) {
      if (field.includes("date_")) {
        if (formulaire.controls[field].value.date_mois != null && formulaire.controls[field].value.date_annee != null) {
          let mois_select = `${formulaire.controls[field].value.date_mois + 1}`;
          let mois = mois_select.length < 2 ? `0${mois_select}` : mois_select;
          let annee_select = formulaire.controls[field].value.date_annee;
          result[field] = `${mois}/01/${annee_select}`;
        } else {
          result[field] = null;
        }
      } else if (field.includes("technologies")) {

        let technos_new_id = formulaire.controls[field].value;

        let add: number[] = []
        technos_new_id.forEach((techno_new_id: number) => {
          if (!technos_old_id.includes(techno_new_id)) {
            add.push(techno_new_id);
          }
        });

        let remove: number[] = []
        technos_old_id.forEach((techno_old_id: number) => {
          if (!technos_new_id.includes(techno_old_id)) {
            remove.push(techno_old_id);
          }
        });

        result[field] = {
          "add": add,
          "remove": remove
        };

      } else if (field.includes("remarques")) {

        let remarques_new = formulaire.controls[field].value;
        let remarques_new_id = remarques_new.map((e: any) => e.remarque_id);

        let add: any[] = [];

        remarques_new.filter((e: any) => e.remarque_id == "New").forEach((remarque_new: any) => {
          add.push(remarque_new.remarque);
        });

        let remove: number[] = [];
        let update: any[] = [];
        remarques_old_id.forEach((remarque_old_id: any) => {

          if (!remarques_new_id.includes(remarque_old_id)) {
            remove.push(remarque_old_id);
          }

          if (remarques_new_id.includes(remarque_old_id)) {
            let remarque_new = remarques_new.find((e: any) => e.remarque_id == remarque_old_id);
            let remarque_old = remarques_old.find((e: any) => e.remarque_id == remarque_old_id);
            if (remarque_new.remarque != remarque_old.remarque) {
              update.push({
                "remarque_id": remarque_old_id,
                "remarque": remarque_new.remarque
              });
            }
          }
        });

        result["remarques"] = {
          "add": add,
          "remove": remove,
          "update": update,
        }
      } else {
        result[field] = formulaire.controls[field].value;
      }
    }

    return result;
  }

  public createExperience(data: any) {

    delete data.experience_id;

    let url = `http://127.0.0.1:5000/experience`;
    this.dataService.postData(url, data).subscribe((response) => {
      console.log(response);
    });
  }

  public updateExperience(data: any) {
    let url = `http://127.0.0.1:5000/experience/${data.experience_id}`;
    this.dataService.postData(url, data).subscribe((response) => {
      console.log(response);
    });
  }

  public deleteExperience(formulaire: FormGroup) {
    let url = `http://127.0.0.1:5000/experience/${formulaire.controls["experience_id"].value}`;
    this.dataService.deleteData(url).subscribe((response) => {
      console.log(response);
    });
  }
}
