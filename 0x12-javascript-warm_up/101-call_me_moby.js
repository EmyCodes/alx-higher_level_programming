#!/usr/bin/node
function callMeMoby (x, theFunction) {
  if (typeof x !== 'number') {
    x = parseInt(x);
  }
  if (typeof theFunction !== 'function') {
    theFunction = function () {};
  }
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Or

/**
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
**/
module.exports.callMeMoby = callMeMoby;
