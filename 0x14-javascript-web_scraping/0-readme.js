#!/usr/bin/node
// Import fs module
const fs = require('fs');

// Assign file path
const filePath = process.argv[2];

// Read the file and print its content
fs.readFile(filePath, 'utf-8', function (error, fileContent) {
  if (error) {
    console.error(error);
  } else {
    console.log(fileContent);
  }
});
