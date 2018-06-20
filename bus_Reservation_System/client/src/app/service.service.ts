import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})

export class ServiceService {
    url = 'http://localhost:8000/travel_list';
    cpHeaders = new Headers({ 'Content-Type': 'application/json' });
    options = new RequestOptions({ headers: this.cpHeaders });
  
    constructor(private _http: Http) { }

    getTravelInfo() {
      return this._http.get(this.url, this.options)
        .pipe(map((response: Response) => response.json()));
        
    }

}
