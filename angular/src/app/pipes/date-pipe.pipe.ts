import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'datePipe'
})
export class DatePipePipe implements PipeTransform {

  public jour = "dd";
  public mois = "mm";
  public moisEntier = "MM";
  public listMoisEntier = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
  public annee = "yyyy";

  transform(value: any, to = "dd/mm/yyyy", from = "mm/dd/yyyy"): unknown {
    if (typeof value == "string") {
      let indexJour = from.indexOf(this.jour);
      let indexMois = from.indexOf(this.mois);
      let indexAnnee = from.indexOf(this.annee);

      let jour = value.slice(indexJour, indexJour+this.jour.length);
      let mois = value.slice(indexMois, indexMois + this.mois.length);
      let moisEntier = this.listMoisEntier[parseInt(mois)];
      let annee = value.slice(indexAnnee, indexAnnee + this.annee.length);
      
      to = to.replace(this.jour, jour);
      to = to.replace(this.mois, mois);
      to = to.replace(this.moisEntier, moisEntier);
      to = to.replace(this.annee, annee);

      return to;
    }
    return null;
  }

}
