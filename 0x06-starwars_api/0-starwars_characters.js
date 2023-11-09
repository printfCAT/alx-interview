#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  return new Promise((resolve, reject) => {
    request({ uri: `https://swapi-api.alx-tools.com/api/films/${movieId}`, json: true }, (filmError, filmResponse, filmBody) => {
      if (filmError) {
        reject(new Error(`Error fetching film data: ${filmError.message}`));
      } else {
        const { characters } = filmBody;
        const characterPromises = characters.map((characterUrl) => new Promise((characterResolve, characterReject) => {
          request({ uri: characterUrl, json: true }, (characterError, characterResponse, characterBody) => {
            if (characterError) {
              characterReject(new Error(`Error fetching character data: ${characterError.message}`));
            } else {
              characterResolve(characterBody.name);
            }
          });
        }));

        Promise.all(characterPromises)
          .then((characterNames) => resolve(characterNames))
          .catch((characterError) => reject(characterError));
      }
    });
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

getCharacters(movieId)
  .then((characterNames) => {
    characterNames.forEach((name) => console.log(name));
  })
  .catch((error) => console.error(`Error: ${error.message}`));
