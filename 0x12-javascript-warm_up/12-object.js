#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
this.value = 98;
console.log(myObject);
