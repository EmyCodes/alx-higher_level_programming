#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      // Do nothing if width or height is not defined
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }

  double () {
    const doubleWidth = this.width * 2;
    const doubleHeight = this.height * 2;
    for (let i = 0; i < doubleHeight; i++) {
      console.log('X'.repeat(doubleWidth));
    }
  }
}
module.exports = Rectangle;