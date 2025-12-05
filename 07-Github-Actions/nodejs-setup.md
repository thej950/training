# Nodejs Code Initialize Process from starting 
## 1. Nodejs project structure
```bash
project/
│── index.js
│── package.json
│── tests/
│     └── app.test.js
```

Here is the **complete step-by-step flow from scratch** — exactly how you will do it on your system.

---

# ✅ **1. Create a new Node.js project**

```sh
npm init -y
```

This creates a default `package.json`.

---

# ✅ **2. Install Express**

```sh
npm install express
```

---

# ✅ **3. Install Jest (dev dependency)**

```sh
npm install --save-dev jest
```

---

# ✅ **4. Update package.json test script**

Open `package.json` → replace test script:

**Before**

```json
"test": "echo \"Error: no test specified\" && exit 1"
```

**After**

```json
"test": "jest"
```

---

# ✅ **5. Create index.js**

`index.js`

```js
function sum(a, b) {
  return a + b;
}

console.log("sum(3,5) =", sum(3, 5));

module.exports = sum;
```

---

# ✅ **6. Create test folder and test file**

```sh
mkdir tests
```

Create `tests/app.test.js`

```js
const sum = require("../index");

test("adds two numbers", () => {
  expect(sum(3, 5)).toBe(8);
});
```

---

# ✅ **7. Run Tests**

```sh
npm test
```

Expected output:

```
PASS  tests/app.test.js
✓ adds two numbers (5 ms)
```

---

# 🎯 Summary

| Step            | Command                       |
| --------------- | ----------------------------- |
| Init project    | `npm init -y`                 |
| Install express | `npm install express`         |
| Install jest    | `npm install --save-dev jest` |
| Run tests       | `npm test`                    |

---
