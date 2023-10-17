#!/usr/bin/node
const myObjects = {
  type: 'object',
  value: 12
};
console.log(myObjects);

myObjects.incr = function () {
  myObjects.value += 1;
};

myObjects.incr();
console.log(myObjects);
myObjects.incr();
console.log(myObjects);
myObjects.incr();
console.log(myObjects);
