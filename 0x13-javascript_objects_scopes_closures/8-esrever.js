#!/usr/bin/noder/bin/node
// function that returns the reversed version of a list.
exports.esrever = function (list) {
  let i = (list.length - 1);
  const newList = [];

  while (i >= 0 && list[i]) {
    newList.push(list[i]);
    i -= 1;
  }
  return (newList);
};
