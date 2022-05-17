#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(argv[0], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
