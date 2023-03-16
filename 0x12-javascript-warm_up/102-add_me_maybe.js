#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  if (typeof number !== 'number') {
    number = parseInt(number); // number = +number;
  }

  if (typeof theFunction !== 'function') {
    theFunction = function () {};
  }

  number++; // Or ++number;

  theFunction(number);
}
module.exports.addMeMaybe = addMeMaybe;
