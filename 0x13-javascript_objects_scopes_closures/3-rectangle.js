#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    // method to print a X square
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width))
    }
  } 
}
module.exports = Rectangle;
