import assert from "node:assert/strict";
import { greet } from "../src/greet.js";

assert.equal(greet("Wuwei"), "Hello, Wuwei!");
assert.equal(greet(""), "Hello, World!");

console.log("greet.test.js passed");
