#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

let firstArgum = process.argv[2];
firstArgum = parseInt(firstArgum);
console.log(factorial(firstArgum));
