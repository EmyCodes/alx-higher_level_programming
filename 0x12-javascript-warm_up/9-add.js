#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

const arg1_int = parseInt(arg1);
const arg2_int = parseInt(arg2);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

if (arg1 === undefined || arg2 === undefined) {
  console.log('NaN');
} else {
  add(arg1_int, arg2_int);
}
