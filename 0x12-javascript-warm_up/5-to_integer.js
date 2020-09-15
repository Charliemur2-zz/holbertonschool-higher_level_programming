#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Not a number');
} else if (parseInt(process.argv[2])) {
  console.log('My number is: ' + (parseInt(process.argv[2])));
} else {
  console.log('Not a number');
}
