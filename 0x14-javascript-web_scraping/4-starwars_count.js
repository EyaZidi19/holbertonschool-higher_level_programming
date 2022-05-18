#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const find = '/18/';
request(process.argv[2], function (error, response, body) {
  if (error) throw new Error(error);
  let times = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      times += (character.includes(find) ? 1 : 0);
    }
  }
  console.log(times);
});
