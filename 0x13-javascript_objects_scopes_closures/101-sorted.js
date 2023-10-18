#!/usr/bin/node
const dict = require('./101-data').dict;
const newDicts = {};

for (const keys in dict) {
  if (!newDicts[dict[keys]]) {
    newDicts[dict[keys]] = [keys];
  } else {
    newDicts[dict[keys]].push(keys);
  }
}

console.log(newDicts);
