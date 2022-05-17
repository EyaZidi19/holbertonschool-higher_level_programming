#!/usr/bin/node
// script that display the status code of a GET request
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
