#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let element = list.length - 1; element >= 0; element--) {
    reversed.push(list[element]);
    // return reversed;
  }
  return reversed;
};
