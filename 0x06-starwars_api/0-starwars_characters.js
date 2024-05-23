#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data, Status Code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  // Function to get character names from URLs
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  // Array to hold promises for each character
  const characterPromises = charactersUrls.map(getCharacterName);

  // Wait for all promises to resolve
  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error('Error fetching character data:', error);
      process.exit(1);
    });
});
