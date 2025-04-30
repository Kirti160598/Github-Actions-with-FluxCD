# 🚀 Flask App CI/CD with GitHub Actions and FluxCD

This project demonstrates a complete DevOps pipeline to build, test, containerize, and deploy a Flask app using **GitHub Actions** for CI and **FluxCD** for GitOps-based Kubernetes deployment.

---

## 🔁 CI/CD Workflow

1. ✅ Code change in the Flask app is **pushed to GitHub**
2. 🧪 **GitHub Actions** is triggered (`on: push`)
3. 🐳 A **Docker image** is built by GitHub actions.
4. 🔖 The image is **tagged** uniquely.
5. 📤 The image is **pushed** to a Docker registry (e.g., Docker Hub)
6. 📝 `deployment.yaml` is updated with the new tag.
7. 🧾 The updated manifest deployment.yaml is committed back to the GitOps repo (watched by FluxCD)
8. 👀 FluxCD detects the manifest change and applies it to the Minikube cluster
9. 📦 Kubernetes pulls the new image and updates the pod
10. 🚀 The updated Flask app is live

## Setting Up FluxCD with Minikube and GitHub Actions
 Step 1: Set up Docker Desktop for Windows.
 
 Step2:  Set up Minikube Cluster and start:
 
```minikube start```

Step 3. Install Flux CLI on local machine.

Step4. Map FluxCD to the Correct Minikube Cluster

```  kubectl config use-context minikube```

Step 5. Bootstrap the Flux CD with github repo and K8s:

```flux bootstrap github   --owner=Kirti160598   --repository=Github-Actions-with-FluxCD   --branch=main   --path=./k8s   --personal```

 It will ask Personal Github Token generate from github and apply.
 
While bootstrapping it will install and initialize the flux CD inside k8s cluster.

Step 6.Try running the image locally to check if the build is fine:

```docker run -p 5000:5000 kirtigupta1234/github-flux-demo:latest-1745923076```

Step 7. Port Forward to Test Locally

```kubectl port-forward svc/github-flux-demo-service 8080:80 -n flux-system```

Step 8.Inspect the Flux pods and logs:

```kubectl get pods -n flux-system```

```kubectl logs -n flux-system deploy/kustomize-controller```

Step9. Observe Flux Reconciliation

After pushing changes to GitHub:

```flux get kustomizations -A```

To see the sync status, last applied revision, and any errors.

Example:

```flux get kustomizations -n flux-system```

Step 10. Manual trigger reconciliation:

```flux reconcile kustomization flux-system --with-source```





