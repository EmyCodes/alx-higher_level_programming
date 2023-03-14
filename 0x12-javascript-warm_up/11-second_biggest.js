#!/usr/bin/node
const args = process.argv.slice(2);

function secondLargestNumber (numbers) {
  // Convert the arguments to an array of integers
  const arr = numbers.map(num => parseInt(num));

  // Check if the array has at least two elements
  if (arr.length < 2) {
    return 0;
  }

  // Sort the array in descending order
  const sortedArr = arr.sort((a, b) => b - a);

  // Find the second largest number in the array
  let secondLargest = sortedArr[1];
  for (let i = 2; i < sortedArr.length; i++) {
    if (sortedArr[i] < secondLargest) {
      return secondLargest;
    } else {
      secondLargest = sortedArr[i];
    }
  }

  return secondLargest;
}

console.log(secondLargestNumber(args));
