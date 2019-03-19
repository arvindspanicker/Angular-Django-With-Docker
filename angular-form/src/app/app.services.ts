import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {HttpParams} from '@angular/common/http';
import {HttpHeaders} from '@angular/common/http';


@Injectable()
export class ConfigService {
    constructor(private httpClient: HttpClient) { }

    /**
   * GET
   * @param url : url;
   */   
    httpGet(url: any): Observable<any> {
        return this.httpClient.get(url);
    }

    httpPost(url: any, body?: any): Observable<any> {

        let headers = new HttpHeaders()
        .set('Content-Type', 'application/json');
        return this.httpClient.post(url, body, {
          headers: headers,
          responseType: 'text'
        });
      }
}

