#!/usr/bin/node
exports.esrever = function (list) {
  const newLists = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newLists.push(list[i]);
  }
  return newLists;
};
