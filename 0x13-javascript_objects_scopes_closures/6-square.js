#!/usr/bin/node

const importedSquare = require('./5-square.js');
module.exports = class Square extends importedSquare {
  constructor (length) {
    super(length);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
