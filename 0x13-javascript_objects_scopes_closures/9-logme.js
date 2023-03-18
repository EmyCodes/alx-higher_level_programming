#!/usr/bin/node
let rollNo = 0;
exports.logMe = function (item) {
  const result = `${rollNo}: ${item}`;
  console.log(result);
  rollNo++;
};
