
# Replication Controller & ReplicaSet & Deployment 
<details>
  <summary><b>Working With Replication Controller, ReplicaSet & Deployment</b></summary>

- **Replication** (High Availability, Load Balancing, Scalability)

- **ReplicationController (rc)** → Control Plane → Controller Manager

- rc contains the **pod template**, meaning whenever rc creates pods, it uses this definition.

- rc identifies pods using **pod labels**.  
  It uses a **label selector** to pick the matching pods.


```bash
notepad rc.yaml
cd C:\fractalTraining\kubernetes\
kubectl get pods
kubectl create -f .\rc.yaml
kubectl create -f .\rc.yaml
kubectl get rc
kubectl get pods -o wide
# lets delete one of the pod and let's c that rc creates a new one or not
kubectl delete pod nginx-rc-dh6fb
kubectl get pods -o wide
kubectl run pod2 --image nginx
kubectl get pods
kubectl get pods -l app=nginx-app
# if we delete the rc then all the pods related to rc will be deleted
kubectl delete -f .\rc.yaml
kubectl get pods
kubectl get rc
# Replicaset is the next generation of rc, because if uses the match expression which is called the  set based ex…
kubectl create -f .\rs.yaml
kubectl get rs
kubectl get pods
kubectl describe rs nginx-rs
kubectl get pods -l app=nginx-app
kubectl get pods -l 'frontedn in (web)'
kubectl get pods -l 'frontend in (web)'
kubectl delete -f .\rs.yaml
```
</details>

<details>
  <summary><b>Deployment in Kubernetes (Simple Explanation)</b></summary>

- **Deployment is used to deploy applications** or update the version of an application.
- A **Deployment uses ReplicaSet (rs)** in the background to maintain the desired number of pods.
- The main purpose of a Deployment is to **ensure zero downtime during updates**.
- It follows the **Rolling Update strategy**, similar to Blue-Green style updates.
- That means **old pods are gradually replaced with new pods** while keeping the application running.

### Example Scenario:
- Create a deployment with **nginx:1.28.0**
- Update the deployment to **nginx:1.29.3**
- Perform rollout, check rollout status, and rollback if needed.



```bash
kubectl create deploy nginx-deploy --replicas 1 --image nginx
kubectl get all
kubectl create deploy nginx-deploy --replicas 1 --image nginx --dry-run=client-o yaml
kubectl create deploy nginx-deploy --replicas 1 --image nginx --dry-run=client -o yaml
kubectl delete deploy nginx-deploy
kubectl get all
kubectl create -f .\deploy.yaml
kubectl get all
kubectl get all
kubectl apply -f .\deploy.yaml
kubectl get all
kubectl get all
kubectl delete deploy nginx-deploy
kubectl create -f .\deploy.yaml
kubectl get all
# let's update the docker image for my deploy contianer c1 with invalid docker image, we will notice that there i…
kubectl set image deploy nginx-deploy c1=image1:invalid
kubectl describe deploy nginx-deploy
kubectl describe deploy nginx-deploy | Select-String "revision"
kubectl describe deploy nginx-deploy | Select-String "image"
kubectl get all
kubectl desccribe pod nginx-deploy-7f78c78486-29fzb
kubectl describe pod nginx-deploy-7f78c78486-29fzb
# because we intentionally used the invalid docker image so our deployment is failed but there is no downtime app…
kubectl rollout undo deploy nginx-deploy
kubectl get all
kubectl describe deploy nginx-deploy | Select-String "revision"
kubectl describe deploy nginx-deploy | Select-String "image"
# we can delete the rs which is invalid
kubectl get rs
kubectl delete rs nginx-deploy-7f78c78486
kubectl set image deploy nginx-deploy c1=nginx:1.29.3
kubectl get pods
kubectl rollout undo deploy nginx-deploy
kubectl get pods
kubectl scale deploy nginx-deploy --replicas 3
kubectl get pods
kubectl get pods
kubectl get pods
kubectl set image deploy nginx-deploy c1=nginx:1.29.3
kubectl get pods
kubectl get pods
kubectl get pods
kubectl describe deploy nginx-deploy
kubectl delete deploy --all
kubectl get all
```
</details>

<summary><b>Examples Manifest files Replication Controller, ReplicaSet & Deployment</b></summary>

```bash
# deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  selector:
    matchLabels:
      app: nginx-app
  template:
    metadata:
      labels:
        app: nginx-app
    spec:
      containers:
      - name: c1
        image: nginx:1.28.0
        
```
```bash
#rc.yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-rc
spec:
  replicas: 3
  selector:
    app: nginx-app
  template:
    metadata:
      name: myapp
      labels:
        app: nginx-app
    spec:
      containers:
        - name: myapp
          image: nginx
          ports:
            - containerPort: 80
```


```yaml
# rs.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
  labels:
    app: nginx-app
    frontend: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-app
    matchExpressions:
      - key: frontend
        operator: In
        values:
        - web  
  template:
    metadata:
      labels:
        app: nginx-app
        frontend: web
    spec:
      containers:
        - name: myapp
          image: nginx
```



# Ingress

<details>
  <summary><b>Kubernetes Ingress (Simple Explanation)</b></summary>

- **Ingress allows you to expose multiple services using a single public IP address.**
- Under the Ingress, you usually have **multiple ClusterIP services**, each representing a different application.
- Using Ingress rules, you can route traffic based on:
  - **Path-based routing** (example: /api → api-service)
  - **Host-based routing** (example: app.example.com → frontend-service)
- Ingress uses an **Ingress Controller** (like NGINX, HAProxy, Traefik) to handle actual traffic routing.
- This avoids creating multiple LoadBalancers and reduces cost.
- In short:  
  **One Public IP → Many internal services** via routing rules.

### Example Use Case:
- `/app1` → app1-service  
- `/app2` → app2-service  
- `api.example.com` → backend-service  

</details>

<details>

# Example

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx   # Must match 'kubectl get ingressclass' output
  rules:
  - http:
      paths:
      - path: /news
        pathType: Prefix
        backend:
          service:
            name: news
            port:
              number: 80
      - path: /mail
        pathType: Prefix
        backend:
          service:
            name: mail
            port:
              number: 8080
```


```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.7.1/deploy/static/provi…
kubectl get ns
kubectl get svc -n ingress-nginx
kubectl run news-pod --image nginx
kubectl run mail-pod --image tomcat
kubectl expose pod news-pod --name news --type ClusterIP --port 80 --target-port 80
kubectl expose pod mail-pod --name mail --type ClusterIP --port 8080 --target-port 8080
kubectl get svc
kubectl create -f .\ingress.yaml
kubectl get ingress
kubectl delete -f .\ingress.yaml
kubectl delete svc news
kubectl delete svc mail
kubectl delete pods --all
kubectl delete deploy --all
```
</details>

===

# ConfigMaps
<details>
  <summary><b>ConfigMap in Kubernetes (Simple Explanation)</b></summary>

- **ConfigMap is used for non-sensitive data** and stores values in **key-value pairs**.
- It is mainly used to store **configuration files**, environment variables, or any external data that the application needs.
- Data inside a ConfigMap is stored in **keys and values**, and **should not contain sensitive data** (use Secret for that).
- Whenever you have configurations that **change across environments** (dev, test, prod), we create a ConfigMap and mount it to the application.

### Example Use Cases:
- Storing application config (`app.properties`)
- Passing environment variables to containers
- Mounting config files into pods
- Separating application code from configuration



```bash
kubectl create cm cm-1 --from-file .\stag_web.xml --from-file .\prod_web.xml
kubectl describe cm cm-1
kubectl delete cm cm1
kubectl delete cm cm-1
kubectl create cm cm-1 --from-file .\stag_web.xml --from-file .\prod_web.xml
kubectl get cm
kubectl describe cm cm-1
kubectl get pods
kubectl create -f .\cm-pod.yaml
kubectl describe pod cm-pod
kubectl exec -it cm-pod -- ls /myapp
kubectl exec -it cm-pod -- cat /myapp/web.xml
# secrets are same configmap but it stores the sensitive data (endcoded with base64)
kubectl create secret generic sec-1 --from-literal password=mypassword
kubectl describe secret sec-1
kubectl create -f .\sec-pod.yaml
kubectl get pods
kubectl describe pod sec-pod
kuebctl exec -it sec-pod -- env
kubectl exec -it sec-pod -- env
```
</details>

# Examples Manifest files 

```yaml 
# sec-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sec-pod
  labels:
    app.kubernetes.io/name: myapp
spec:
  containers:
  - name: myapp
    image: nginx
    env:
    - name: password
      valueFrom:
        secretKeyRef:
          name: sec-1
          key: password
```
```yaml
# cm-pod.yaml
#nginx-pod-configmap-vol.yaml

apiVersion: v1
kind: Pod
metadata:
  name: cm-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    volumeMounts:
    - name: test-vol
      mountPath: "/myapp"
      readOnly: true
  volumes:
    - name: test-vol
      configMap:
        name: cm-1
        items:
        - key: stag_web.xml
          path: web.xml
```

# Namespace 
```bash
# namespaces are the virtual cluster where we segregate the resources from different environments
kubectl create ns dev
kubectl get pods
kubectl describe pod cm-pod
kubectl get ns
kubectl delete pods --all
kubectl get pods
kubectl run pod1 --image nginx -n dev
kubectl get pods
kubectl get pods -n dev
# kubeconfig is the file where cluster which we need to connect configuration is available
# that file is available under users folder/.kube/config file
# there are some commands which we can use to access the configuration file
kubectl config view
# context is the way by which you can switch to different namespaces, we need to set 3 values 1. user, namespace,…
kubectl config get-contexts
kubectl config delete-context aks1 arn:aws:eks:ap-south-1:670154208195:cluster/eksdemo1 askcluster-raman  minikube
kubectl config delete-context aks1
kubectl config delete-context minikube
kubectl config delete-context arn:aws:eks:ap-south-1:670154208195:cluster/eksdemo1
kubectl config delete-context askcluster-raman
kubectl config view
kubectl config delete-user minikube
kubectl config delete-user clusterUser_raman_rg_aks1
kubectl config delete-user clusterUser_aksgroup_akscluster
kubectl config delete-user  clusterUser_MyRG_akscluster
kubectl config delete-user  arn:aws:eks:ap-south-1:670154208195:cluster/eksdemo1
kubectl config delete-user  clusterUser_askcluster-raman_group_askcluster-raman
kubectl config view
kubectl config get-contexts
# lets switch to dev namespace to do that we need to create a context
kubectl config get-contexts
kubectl config set-context devcontext --user clusterUser_Training-RG_akscluster --cluster akscluster --namespace …
kubectl config get-contexts
kubectl config use-context devcontext
kubectl config get-contexts
kubectl get pods
# Rolebased access control (RBAC) create a user with limited access to the namespace
# for that we need to create a role (verbs get,create,delete)
# rolebinding attach the role to the user
kubectl config use-context akscluster
kubectl config get-contexts
kubectl config delete-context devcontext
kubectl config get-contexts
kubectl get ns
kubectl delete ns dev
kubectl get pods -n kube-system
kubectl run pod1 --image nginx -n dev --dry-run=client -o yaml
```
===

# Helm 
```bash
# helm charts are package manager in kubernetes
helm --verion
helm --version
helm version
# install helm first https://helm.sh/docs/intro/install/   for windows
# cosider in your project you are having multiple yaml files and you need to execute all yaml files as a package(…
helm create mychart
ls
ls .\mychart\
kubectl delete pods --all
kubectl get all
# let's install helm chart, it create all the resources which is in the templates directory
helm install mypack .\mychart\
helm list
kubectl get all
helm uninstall mypack
kubectl get all
cd .\mychart\templates\
ls
rm -f *.*
rm  *.*
ls
rmdir .\tests\
ls
kubectl run pod1 --image nginx -n dev --dry-run=client -o yaml > pod.yaml
ls
kubectl get all
cd ..
cd ..
helm install mypack .\mychart\
rm .\mychart\templates\*.*
kubectl run pod1 --image nginx  --dry-run=client -o yaml > mychart/templates/pod.yaml
helm install mypack .\mychart\
kubectl get all
ls
cd .\mychart\
cd .\templates\
ls
rm *.*
kubectl run pod1 --image nginx  --dry-run=client -o yaml > pod1.yaml
cd ..
cd ..
helm install mypack1 .\mychart\
helm list
kubectl get all
```