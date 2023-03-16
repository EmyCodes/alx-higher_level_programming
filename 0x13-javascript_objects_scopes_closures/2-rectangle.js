#!/usr/bin/node
'use strict';
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;

      return `Rectangle { width: ${this.width}, height: ${this.height} }`;
    }
  }
}
module.exports = Rectangle;
