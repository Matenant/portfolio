import { Injectable } from "@angular/core";
import { FormArray, FormControl, FormGroup } from "@angular/forms";
import { Observable, Subject } from "rxjs";
import { DataService } from "src/app/services/data.service";

@Injectable({
  providedIn: 'root'
})
export class Categorie {
  public datas: any = [];

  constructor(private dataService: DataService) {

  }

  public getAllCategorie(): Observable<any> {
    var subject = new Subject<any>();
    let url = "http://127.0.0.1:5000/categorie"
    let data = this.dataService.getData(url);
    data.subscribe((response) => {
      this.datas = response;
      subject.next(this.datas);
    });
    return subject.asObservable();
  }
}
