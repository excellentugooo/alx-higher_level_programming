#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arrs = process.argv.slice(2).map(Number);
  console.log(arrs.sort((a, b) => a - b)[arrs.length - 2]);
}
