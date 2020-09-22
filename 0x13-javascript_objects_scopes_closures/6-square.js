#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint(c) {
    if (c) {
      for (let i = 1; i <= this.width; i++) {
      console.log(c.repeat(this.width));
    } else {
      this.print();
    }
  }
}
module.exports = Square;
