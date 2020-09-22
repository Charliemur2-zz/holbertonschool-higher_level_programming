#!/usr/bin/node
const list = require('./100-data').list;
let procesList = []
procesList = list.map(x => x * list.indexOf(x));
console.log(list);
console.log(procesList);
