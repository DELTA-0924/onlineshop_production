
import { Component, Input, ElementRef, AfterViewInit, Renderer2 } from '@angular/core';
@Component({
  selector: 'app-image',
  standalone: true,
  imports: [],
  templateUrl: './image.component.html',
  styleUrl: './image.component.css'
})
export class ProductImageComponent implements AfterViewInit {
  @Input() imageUrl: string;

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  ngAfterViewInit(): void {
    const img = new Image();
    img.src = this.imageUrl;
    let heigth=350
    if(img.height<350)
      heigth=img.height;
    img.onload = () => {
      const div = this.el.nativeElement.querySelector('div');
      this.renderer.setStyle(div, 'width', `${img.width}px`);
      this.renderer.setStyle(div, 'height', `${heigth}px`);
      this.renderer.setStyle(div, 'backgroundImage', `url('${this.imageUrl}')`);
      this.renderer.setStyle(div, 'backgroundSize', 'contain');
      this.renderer.setStyle(div, 'backgroundRepeat', 'no-repeat');
      this.renderer.setStyle(div, 'backgroundPosition', 'center');
    };
    img.onerror = () => {
      console.error("Image not found:", this.imageUrl);
    };
  }
}
