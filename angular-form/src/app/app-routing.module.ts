import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AmazonComponent } from './amazon/amazon.component'
import { OthersComponent } from './others/others.component'


const routes: Routes = [
  {
    path: '',
    redirectTo: 'amazon',
    pathMatch: 'full'
  },
  {
    path: 'amazon',
    component: AmazonComponent
  },
  {
    path: 'others',
    component: OthersComponent
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
