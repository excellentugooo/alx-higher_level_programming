#!/usr/bin/node
const firstArgum = process.argv[2];
if (!firstArgum) {
  console.log('No argument');
} else {
  console.log(firstArgum);
}
