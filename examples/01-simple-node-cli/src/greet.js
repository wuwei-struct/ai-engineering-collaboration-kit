export function greet(name) {
  const safeName = String(name || "World").trim() || "World";
  return `Hello, ${safeName}!`;
}
