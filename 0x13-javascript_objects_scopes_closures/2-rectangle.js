#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle                                                                                        

class Rectangle {
  // create a class Square                                                                                                                        
  constructor (w, h) {
    // constructor for pass arguments in Rectangle class                                                                                          
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
