#!/usr/bin/node
// func that executes x times a fun
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
