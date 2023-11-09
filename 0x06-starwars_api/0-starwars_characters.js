/* eslint-disable linebreak-style */
const request = require('request');

const movieId = process.argv[2];

const options = {
  uri: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const { characters } = body;

  for (const character of characters) {
    console.log(character.name);
  }
});
