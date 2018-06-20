import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
//import { Observable } from 'rxjs/Observable';
import { ServiceService } from './service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {

  title = 'app';
  clientDetails


  constructor(private _service: ServiceService){}
  public getTravelList(){
      this._service.getTravelInfo()
      .subscribe((data) => {
        this.clientDetails = data;
        console.log(this.clientDetails);
      },
      (error) => { console.log(error) })

    }
}

