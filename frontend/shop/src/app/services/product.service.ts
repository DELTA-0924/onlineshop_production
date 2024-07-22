import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, of } from 'rxjs';
import { Product } from '../common/Product';
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private  url:string="/api"
  constructor(private http:HttpClient) { }
  get():Observable<any>{
    let limit=new HttpParams().append("limit",5);
    return this.http.get<any>(`${this.url}/products/`);
  }
  getByCategory(category:string,page:number,pageSize:number):Observable<any>{
    if (category==="Главная")
      category="Main"
    let params=new HttpParams().append("category",category).append("page",page.toString()).append("page_size",pageSize.toString());
    return this.http.get<any>(`${this.url}/category/`,{params:params});
  }
  getCategory():Observable<any>{
    return this.http.get<any>(`${this.url}/categories/`);
  }
  searchProducts(query: string,category:string,page:number,pageSize:number): Observable<any[]> {
      if (category==="Главная")
      category="Main"
    let params=new HttpParams().append("category",category).append("page",page).append("page_size",pageSize).append("query",query);
    return this.http.get<any[]>(`${this.url}/product-search/`,{params:params});
  }
}
