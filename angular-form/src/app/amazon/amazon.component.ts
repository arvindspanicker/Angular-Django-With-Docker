import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../app.services'
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-amazon',
  templateUrl: './amazon.component.html',
  styleUrls: ['./amazon.component.css']
})
export class AmazonComponent implements OnInit {

  public title = 'Amazon Component';
  public config : any ;
  public api_url_for_data :string = 'http://192.168.20.173/api/testapp/v1/amazon/'
  public data : any;
  constructor(private configService: ConfigService) {}

  title_new = new FormControl('');

  showConfig() {
    this.configService.httpGet(this.api_url_for_data)
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
    this.configService.httpPost(this.api_url_for_data,send_data)
      .subscribe((res) => {
        this.showConfig();
        this.title_new = new FormControl('');
    });
  }

}
