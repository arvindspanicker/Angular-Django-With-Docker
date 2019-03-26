import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../app.services'
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-others',
  templateUrl: './others.component.html',
  styleUrls: ['./others.component.css']
})
export class OthersComponent implements OnInit {

  public title = 'Others Component';
  public config : any ;
  public api_url :string = 'http://192.168.20.173/api/testapp/v1/others/'
  public data : any;
  constructor(private configService: ConfigService) {}


  title_new = new FormControl('');

  showConfig() {
    this.configService.httpGet(this.api_url)
      .subscribe((data) => {
         this.data = data;
      });
  }

  ngOnInit(): void {
    this.showConfig();
  }


  save(){
    let send_data = {
      'title': this.title_new.value
    }
    this.configService.httpPost(this.api_url,send_data)
      .subscribe((res) => {
        this.showConfig();
        this.title_new = new FormControl('');
    });
  }

}
