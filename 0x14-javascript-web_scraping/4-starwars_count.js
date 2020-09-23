#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const charUrl = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
let numMovies = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let resultList = JSON.parse(body).results;
    resultList.forEach(function (charactersList) {
      charactersList.characters.forEach(function (character) {
        if (character === charUrl) {
          numMovies++;
        }
      });
    });
    console.log(numMovies);
  }
});
