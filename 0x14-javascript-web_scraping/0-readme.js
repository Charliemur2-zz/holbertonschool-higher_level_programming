#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
try {
  const data = file.readFileSync(argv[2], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
