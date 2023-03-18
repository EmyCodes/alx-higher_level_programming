#!/usr/bin/node

const importedSquare = require('./5-square.js');
module.exports = class Square extends importedSquare {
  constructor (length) {
    super(length);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
	//console.log('X'.repeat(this.width));
    } else {
	for (let i = 0; i < this.height; i++) {
          console.log(c.repeat(this.width));
      }
    }
  }
};
