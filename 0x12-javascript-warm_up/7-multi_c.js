#!/usr/bin/node
const statement = 'C is fun';
const numOfTimes = process.argv[2];
const x = parseInt(numOfTimes);

if (isNaN(numOfTimes)) {
		console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < x; i++) {
		console.log(statement);
	}
}
