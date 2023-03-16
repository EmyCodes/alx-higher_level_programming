#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value = this.value++;
  }
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
