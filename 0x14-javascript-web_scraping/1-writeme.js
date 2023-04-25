#!/usr/bin/node
// a script that writes a string to a file.

// Import error medule and assign variables
const fs = require('fs');
const filePath = process.agrv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf-8', function (error) {
  if (error) {
    console.error(error);
  } else {
    console.log(fileContent);
  }
});
