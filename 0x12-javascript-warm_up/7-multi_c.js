#!/usr/bin/node
let firstArgum = process.argv[2];
if (!firstArgum || isNaN(firstArgum)) {
  console.log('Missing number of occurrences');
} else {
  firstArgum = parseInt(firstArgum);
  for (let i = 0; i < firstArgum; i++) {
    console.log('C is fun');
  }
}
