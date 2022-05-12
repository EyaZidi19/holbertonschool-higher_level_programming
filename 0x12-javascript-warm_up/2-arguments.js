#!/usr/bin/node
//script that prints a message depending of the number of arguments passed 
const len = process.argv.length;

if (len < 3) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
