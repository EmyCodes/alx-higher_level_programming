#!/usr/bin/node
const arg = process.argv[2];
const X = parseInt(arg);
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    console.log('X'.repeat(X));
  }
}
