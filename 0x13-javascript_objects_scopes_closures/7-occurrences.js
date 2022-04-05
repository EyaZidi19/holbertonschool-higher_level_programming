#!/usr/bin/node
// function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let counter = 0;

  while (list[i]) {
    if (searchElement === list[i]) {
      counter += 1;
    }
    i += 1;
  }
  return (counter);
};
