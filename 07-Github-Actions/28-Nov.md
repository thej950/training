
# 12. complete-ci.yml
```yml
name: CI Pipeline

on:
  pull_request:

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
```

# 13. dockerfile
```
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

```

# 14 docker-ci.yml file 

```yml
name: Docker Build (CI)

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          platforms: linux/amd64
          push: false
          tags: myapp:ci
```


13. Build and push the image to dockerhub using GitHub Actions 

```bash
- Generate token in Github with read,write,delete permissions 

- Need to give secrets
   - GitHub->settings->secrets and variables->actions->click on new repository 
    DOCKERHUB_USERNAME: xxxxx
    DOCKERHUB_TOKEN: xxxxxx

```

```yml
name: Docker Build (CI)
on:
  # push:
  #   branches: [ main ]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build docker image
        run: |
          docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/myapp:ci .
      - name: Push docker image
        run: |
          docker push ${{ secrets.DOCKERHUB_USERNAME }}/myapp:ci
```

14. build and push the image to acr using github actions 

```bash
- search Create container registry
- create ACR in Azure, copy(username,login-server,password) 

- Need to give secrets
   - GitHub->settings->secrets and variables->actions->click on new repository 
    ACR_USERNAME: xxxxxx
    ACR_LOGIN_SERVER: xxxxx
    ACR_PASSWORD: xxxxxx

```

![alt text](<.images/Screenshot 2025-12-02 131416.png>)

```yml
name: Docker Build (CI)
on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
     
      - name: Login to Azure Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.ACR_LOGIN_SERVER }}
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}
      - name: Build docker image
        run: |
          docker build -t ${{ secrets.ACR_LOGIN_SERVER }}/myapp:ci .
      - name: Push docker image
        run: |
          docker push ${{ secrets.ACR_LOGIN_SERVER }}/myapp:ci 

```


![alt text](.images/image.png)



===

15. Push the image to GHCR and give read and write permissions for workflow to use to the user
 - create token with required permissions to push image to GHCR 
 - copy token and paste into secrets 

```yml
name: Docker Build (CI)
on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GH_TOKEN }}
      - name: Build docker image
        run: |
          docker build -t ghcr.io/${{ github.repository_owner }}/myapp:ci .
      - name: Push docker image
        run: |
          docker push ghcr.io/${{ github.repository_owner }}/myapp:ci

```

![alt text](.images/image-1.png)




16. Setting Up SelfHosted Runner in GitHub  
  
  ```
  -> Goto CI-CD-Github-Actions repo
  -> Actions
    -> Runners
    -> click on New self Hosted Runner 
  ```

![alt text](.images/github.com_annamthej_CI-CD-Github-Actions_settings_actions_runners_new_arch=x64&os=linux.png)

- Install and Configure 

![alt text](.images/image-2.png)

![alt text](.images/image-3.png)


![alt text](.images/image-4.png)

![alt text](.images/image-5.png)

- Run Below Yaml file for testing 

```bash
name: Hello World Workflow
on:
    push:
        branches:
            - main
jobs:
    hello_world:
     runs-on: self-hosted
     steps:
        - name: Print Hello World
          run: echo "Hello, World!"
        - uses: actions/checkout@v4  
```


- After Ruuning Code will be downloaded into Our Machine      

![alt text](.images/image-6.png)


17. Integrating with  Kubernetes 

  ![alt text](.images/image-7.png)
  
  - To Integrate Github Actions self-Hosted machine with Kuberenetes cluster it needs to authenticated with config file  
  - Copy ~./kube/config file 
  - pste into Github secrets location 
      KUBE_CONFIG_DATA: xxxxxx

 ![alt text](.images/image-8.png)

 ![alt text](.images/image-9.png)

 - After Building 

 ![alt text](.images/image-10.png)





