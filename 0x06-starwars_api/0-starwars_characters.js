#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, function (error, response, body) {
  if (response.statusCode === 200) {
    const parsedData = JSON.parse(body);
    const characterAPIList = parsedData.characters;

    printNames(characterAPIList, 0);
  } else {
    console.log(error);
  }
});

const printNames = (characterAPIList, index) => {
  if (index === characterAPIList.length) {
    return;
  }

  request(characterAPIList[index], function (err, res, body) {
    if (res.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printNames(characterAPIList, index + 1);
    } else {
      console.log(err);
    }
  });
};
