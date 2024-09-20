#!/usr/bin/node

/**
 * helper function for request
 * @param   {String} url - request url
 * @returns {Promise}    - promise object that resolves
 *                         with parsed JSON response
 *                         and rejects with the request error.
 */

function getRequest (url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * makes requests to API and prints the character names
 * for movie info based on first positional argument passed.
 */

async function displayMovieCharacters () {
  const args = process.argv;

  if (args.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  const movie = await getRequest(movieUrl);

  if (!movie.characters) return;
  for (const requestUrl of movie.characters) {
    const character = await getRequest(requestUrl);
    console.log(character.name);
  }
}

displayMovieCharacters();
