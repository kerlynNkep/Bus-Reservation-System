import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import  { ServiceService } from './service.service';
 

@NgModule({
    declarations: [
      AppComponent
    ],
    imports: [
      BrowserModule,
      HttpModule  //this is the Http module. We use the http module to send AJAX/Http request to REST API
    ],
    providers: [ServiceService],
    bootstrap: [AppComponent]
})
export class AppModule { }
