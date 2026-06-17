#!/usr/bin/env node
import { greet } from "./greet.js";

const name = process.argv[2] || "World";
console.log(greet(name));
