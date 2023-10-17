#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

let firstArgum = process.argv[2];
let secondArgum = process.argv[3];

firstArgum = parseInt(firstArgum);
secondArgum = parseInt(secondArgum);

add(firstArgum, secondArgum);
