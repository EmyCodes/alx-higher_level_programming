#!/usr/bin/node

//  a script that display the status code of a GET request.

// import request and declare needed variables
const request = require('request');
const url = process.argv[2];

// Querying the url
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
