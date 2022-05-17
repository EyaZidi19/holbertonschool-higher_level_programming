#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const argv = process.argv.slice(2);
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + argv[0];

request(endpoint, function (error, respose, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
