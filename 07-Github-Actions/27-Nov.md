# Let's Start GithubAction Concepts
 
1. Create a Repository in GitHub called CICDPipeLine-GithubAction
2. Create a Folder Called GithubAction (you can create with any name) and open it in VSCode
3. Install Nodejs and check the version using node -v and npm -v command
4. In VSCode Add the extension GitHub Action from GitHub, GitHub Co-pilot
5. Initialize the git local Repo and push the code to remote repo 
6. Create test.html file and commit it locally and then push to the remote repo







name: CI pipeline
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Printing a message
        run: echo "Hello, World!"
      - name: Show Current time
        run: date
      - name: List files
        run: ls -la
      - name: Print Workflow event
        run: echo "${{ github.event_name }}"
      - name: Show GitHub workspace
        run: echo "${{ github.workspace }}"
      - name: Show Runner OS
        run: echo "${{ runner.os }}"
      - name: Show Github Repository
        run: echo "${{ github.repository }}"


6. Create index.js file with following content
function sum(a, b) {
    return a + b;
}
console.log("Sum(2,3)=", sum(2, 3));
module.exports = sum;

7. Create the test directory
create file app.test.js file
code
console.log("Tested Successfully")

8. Create .gitignore file and write below content
node_modules/






10. Create the Node.yaml file under workflows folder
name: Node.js CI
on: [ push, pull_request]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v4
        - name: Setup Node.js
          uses: actions/setup-node@v4
          with:
            node-version: '20'
        - name: Print Node.js version
          run: node -v
        - name: Print npm version
          run: npm -v      
        - name: Install dependencies
          run: npm install
        - name: Run tests
          run: npm test



11. We can also create the parallel jobs 

    job1 is running in parallel to another job

    we are using keyword needs which allows jobs to run in sequential way
 
name: Parallel Jobs

on: [push]

jobs:

  job1:

    runs-on: ubuntu-latest

    steps:

      - name: Job 1 - Print Message

        run: echo "This is Job 1"

  job2:

    needs: job1    

    runs-on: ubuntu-latest

    steps:

      - name: Job 2 - Print Message

        run: echo "This is Job 2"

  job3:

    needs: job2    

    runs-on: ubuntu-latest

    steps:

      - name: Job 3 - Print Message

        run: echo "This is Job 3"
 

 ===

 name: CI Pipeline
 
on:
  pull_request:
  push:
    branches: [ main ]
 
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
     
      - uses: actions/setup-node@v4
        with:
          node-version: 20
 
      - name: Install dependencies
        run: npm ci
 
      - name: Run linter
        run: npm run lint --if-present
 
  test:
    runs-on: ubuntu-latest
    needs: lint
    strategy:
      matrix:
        node: [18, 20]
 
    steps:
      - uses: actions/checkout@v4
     
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
 
      - name: Cache dependencies
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: ${{ runner.os }}-npm-${{ hashFiles('package-lock.json') }}
 
      - name: Install dependencies
        run: npm ci
 
      - name: Run unit tests
        run: npm test --if-present
 
      - name: Upload test coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage-${{ matrix.node }}
          path: coverage/
 
  build:
    runs-on: ubuntu-latest
    needs: test
 
    steps:
      - uses: actions/checkout@v4
 
      - uses: actions/setup-node@v4
        with:
          node-version: 20
 
      - name: Install dependencies
        run: npm ci
 
      - name: Build project
        run: npm run build --if-present
 
      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/
 
  integration-tests:
    runs-on: ubuntu-latest
    needs: build
 
    steps:
      - uses: actions/checkout@v4
 
      - uses: actions/setup-node@v4
        with:
            node-version: 20
 
      - name: Upload integration test logs
        uses: actions/upload-artifact@v4
        with:
          name: integration-logs
          path: logs/
 
  report:
    runs-on: ubuntu-latest
    needs: [build, test, integration-tests]
 
    steps:
      - name: Final summary
        run: echo "CI pipeline completed successfully."
 


===
Dockerfile
 
# Stage 1: Builder
FROM node:20-alpine AS builder
WORKDIR /app
RUN mkdir -p /app/dist
 
COPY index.js /app/dist/index.js
COPY package*.json ./
RUN npm ci
 
COPY . .
RUN npm run build --if-present
 
# Stage 2: Production image
FROM node:20-alpine AS prod
WORKDIR /app
 
COPY --from=builder /app/dist ./dist
COPY package*.json ./
 
RUN npm ci --only=production
 
CMD ["node", "dist/index.js"]
 