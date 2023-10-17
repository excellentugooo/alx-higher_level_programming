#!/usr/bin/node
let firstArgum = process.argv[2];
if (!firstArgum || isNaN(firstArgum)) {
  console.log('Missing size');
} else {
  firstArgum = parseInt(firstArgum);
  for (let i = 0; i < firstArgum; i++) {
    console.log('X'.repeat(firstArgum));
  }
}
