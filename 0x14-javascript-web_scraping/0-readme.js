#!/usr/bin/node
// Import fs module
const fs = require(''fs)

// Assign file path
const filePath = process.argv[2]

// Read the file and print its content
fs.readFile(filePath, 'utf-8', (error, fileContent) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
