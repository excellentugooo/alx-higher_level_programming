#!/usr/bin/node
let firstArgum = process.argv[2];
if (!firstArgum || isNaN(firstArgum)) {
  console.log('Not a number');
} else {
  firstArgum = parseInt(firstArgum);
  console.log('My number: ' + firstArgum);
}
