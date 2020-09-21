#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print Rectangle object
  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to exchange width and height values
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Method to incrase width and height values by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
