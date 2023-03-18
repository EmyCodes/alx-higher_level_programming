#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      counter++;
    }
  }
  /* Or
  for (const element of list) {
    if (element === searchElement) {
      counter++;
     }
  }
*/
  return counter;
};
