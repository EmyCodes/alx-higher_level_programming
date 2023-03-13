#!/usr/bin/node
const statement = 'C is fun';
const x = process.argv[2];
const numOfTimes = parseInt(x);

if (isNaN(numOfTimes)) {
		console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < numOfTimes; i++) {
		console.log(statement);
	}
}
