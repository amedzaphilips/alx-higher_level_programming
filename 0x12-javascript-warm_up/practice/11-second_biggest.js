#!/usr/bin/node
const myArgs = process.argv.slice(2).map(Number);
if (myArgs.length <= 1) {
	console.log(0);
} else {
	myArgs.sort((a, b) => a - b);
	console.log(myArgs[myArgs.length - 2]);
}
