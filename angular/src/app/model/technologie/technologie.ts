import { Injectable } from "@angular/core";
import { FormArray, FormControl, FormGroup } from "@angular/forms";
import { Observable, Subject } from "rxjs";
import { DataService } from "src/app/services/data.service";

@Injectable({
  providedIn: 'root'
})
export class Technologie {
  public datas: any = [];

  constructor(private dataService: DataService) {
    
  }

  public getAllTechnologie(): Observable<any> {
    var subject = new Subject<any>();
    let url = "http://127.0.0.1:5000/technologie"
    let data = this.dataService.getData(url);
    data.subscribe((response) => {
      this.datas = response;
      subject.next(this.datas);
    });
    return subject.asObservable();
  }
  
}
