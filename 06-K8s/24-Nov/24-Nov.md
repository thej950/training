# Install azcli & kubectl tools 

# After creation AKS it provides two commands 
**Login to your azure account**
```bash
az login
```
**Set the cluster subscription**
```bash
az account set --subscription 4ebfd8f1-7e8d-43d4-9c0c-146f9aa136f6
```
**Download cluster credentials**
```bash
az aks get-credentials --resource-group Practice-RG-01 --name practice-eks --overwrite-existing
```

**How to find the nodes (Worker nodes ) in the cluster**
```bash
kubectl get nodes
```

# Pod 
 - it is the basic or atomic unit for the kubernetes. Pod is the wrapper for the container(s), Pods are getting c…
 - Pod is created by using kubectl commands or by using yaml file (manifest)

**let's create a pod with nginx docker image**
```bash
kubectl run pod1 --image nginx

kubectl get pods

kubectl get pods -o wide

kubectl proxy

kubectl get pod pod1 -o yaml

kubectl describe pod pod1

kubectl logs pod1

kubectl delete pod pod1
```
===

# yaml manifest files
- Manifest file is the way to create kubernetes resources using yaml file
- you can create manifest file using kubernetes command (--dry-run=client -o yaml) means if kuberenetes is havi…

```bash
kubectl run pod1 --image nginx --dry-run=client -o yaml
kubectl run pod1 --image nginx --dry-run=client -o yaml > pod1.yaml

kubectl run pod1 --image nginx --dry-run=client -o yaml > pod1.yaml
rm *.yaml
kubectl run pod1 --image nginx --dry-run=client -o yaml > pod1.yaml
```

**Examples**
```yaml
#notepad-pod.yaml
apiVersion: v1
kind: Pod
metadata:
 name: multic-pod
 labels:
   name: textpad
spec:
 containers:
 - name: c1
   image: nginx
   ports:
     - containerPort: 80
   resources:
     limits:
       memory: "128Mi"
       cpu: "500m"    
 - name: c2
   image: tomcat 
   ports:
     - containerPort: 8080
   resources:
       limits:
         memory: "128Mi"
         cpu: "500m"
```

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: vs-pod
  labels:
    app.kubernetes.io/name: vspod
spec:
  containers:
  - name: vspod
    image: nginx
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
```

**To create the resource(like pod) through manifest file we have kubectl create -f (to create the resource), kube…**

```bash
kubectl create -f .\pod1.yaml
kubectl get pods
```

**To create the pod is using command and 2 way is using --dry-run=client -o yaml 3. using kuberenetes document…**

**let create pod using kubernetes documentation**
```bash
notepad mypod.yaml
kubectl create -f mypod.yaml
kubectl get pods
kubectl get pods
kubectl get pods
kubectl get pods
kubectl get pods
kubectl delete pods --all
kubectl get pods
kubectl get pods
kubectl get pods
watch kubectl get pod
kubectl get pods
```

**lets go inside the container or pod, whenever you go inside the pod you are basically going inside the containe…**
```bash
kubectl run pod1 --image nginx
kubectl get pods
kubectl get pods
kubectl get pods
# lets go inside pod1
kubectl exec -it pod1 -- bash
kubectl exec -it pod1 -- ls
kubectl exec -it multic-pod -c c1 -- ls
kubectl exec -it multic-pod -c c2 -- ls
# whenever we create multicontainer pods then these containers are local host to each other
kubectl exec -it multic-pod -c c1 -- curl localhost
kubectl exec -it multic-pod -c c1 -- curl localhost:8080
kubectl delete pods --all
```

# NodeSelector & affinity & taint & tolerations 

**Examples manifest file**

```bash
# nodeAffinity.yaml
apiVersion: v1
kind: Pod
metadata:
  name: na-pod
  labels:
    app.kubernetes.io/name: na-pod
spec:
  containers:
  - name: na-pod
    image: nginx
  
  affinity:
   nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: env
          operator: In
          values:
          - stag
          - test
    
# nodeName.yaml
apiVersion: v1
kind: Pod
metadata:
  name: node1-pod
  labels:
    app.kubernetes.io/name: node1-pod
spec:
  containers:
  - name: node1-pod
    image: nginx
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
  nodeName: aks-agentpool-54867566-vmss000001      


# nodeSelector.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nodeselector-pod
  labels:
    app.kubernetes.io/name: node1-pod
spec:
  containers:
  - name: node1-pod
    image: nginx
    ports:
      - containerPort: 80
  nodeSelector:
   env: prod  

# taint.yaml
apiVersion: v1
kind: Pod
metadata:
  name: toleration-pod
  labels:
    app.kubernetes.io/name: myapp
spec:
  containers:
  - name: myapp
    image: nginx
  tolerations:
  - key: "app" 
    operator: "Equal"
    value: "blue"
    effect: "NoSchedule"      

```
## Commands
```bash
# next is to create a pod on a specific worknode
kubectl get nodes
kubectl get pods
# master node which also known as control plane has a component called scheduler which decides that where a pod w…
kubectl create -f .\nodeName.yaml
kubectl get pods -o wide
# create a pod on specific category of the worker node, for this we need to define the label on node level, label…
kubectl get nodes --show-labels
# you can see many labels which are predefined, but lets create our own labels to nodes
kubectl get nodes
kubectl label nodes aks-agentpool-54867566-vmss000001 env=stag
kubectl label nodes aks-agentpool-54867566-vmss000000 env=prod
kubectl get nodes --show-labels
# now let's create the pod on prod machine
kubectl create -f .\nodeSelector.yaml
kubectl create -f .\nodeSelector.yaml
kubectl get pods -o wide
kubectl get pods -o wide
kubectl get pods -o wide
kubectl delete pods --all
kubectl create -f .\nodeSelector.yaml
kubectl get pods -o wide
kubectl get pods -o wide
kubectl describe pod nodeselector-pod
kubectl get nodes --show-labels
kubectl delete pods --all
kubectl create -f .\nodeSelector.yaml
kubectl get pods -o wide
# node Affinity ( same as node selector) but it has 2 options 1. requiredDuringSchedulingIgnoreDuringExecution 2.…
kubectl create -f .\nodeAffinity.yaml
kubectl create -f .\nodeAffinity.yaml
kubectl create -f .\nodeAffinity.yaml
kubectl get pods -o wide
kubectl delete pods --all
# Taints :- Property which is on node-level and whenever a pod is tainted then it is expecting a pod with tolerat…
# there are 3 effects which we can use with taints 1. NoSchedule/NoExecute (means the pods without matching toler…
kubectl describe node
kubectl describe node | Select-String "Taints"
kubectl get nodes
kubectl describe node aks-agentpool-54867566-vmss000000| Select-String "Taints"
kubectl describe node aks-agentpool-54867566-vmss000001| Select-String "Taints"
kubectl describe node aks-agentpool-54867566-vmss000004| Select-String "Taints"
kubectl taint nodes aks-agentpool-54867566-vmss000000 app=blue:NoSchedule
kubectl describe node aks-agentpool-54867566-vmss000000| Select-String "Taints"
kubectl run pod1 --image nginx
kubectl get pods -o wide
kubectl run pod2 --image nginx
kubectl get pods -o wide
kubectl delete pods --all
kubectl create -f .\taint.yaml
kubectl get pods -o wide
# we can delete the taint value of the node
kubectl taint nodes aks-agentpool-54867566-vmss000000 app -
kubectl taint nodes aks-agentpool-54867566-vmss000000 app-
kubectl describe node aks-agentpool-54867566-vmss000000| Select-String 
```