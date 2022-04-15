# make sure to use the minikube context
kubectl config use-context minikube

# make docker use the docker daemon inside the kubernetes cluster (and not your local docker install)
eval $(minikube docker-env)

# pull mariadb image from docker
docker pull mariadb

# build the docker image from our fast-api app and tag it with tag 'fast-api'
docker build --rm -t fast-api ../apps/fastapi/.

# delete current deployments and services to force new built images to be used
kubectl delete -n default deployment api-deployment
kubectl delete -n default deployment mariadb
kubectl delete -n default service fast-service
kubectl delete -n default service mariadb

# make kubernetes build everything we specified in the yaml files
kubectl apply -f ./templates/api-secrets.yml --namespace=default
kubectl apply -f ./templates/mariadb-pv.yml --namespace=default
kubectl apply -f ./templates/mariadb-deployment.yml --namespace=default
kubectl apply -f ./templates/api-deployment.yml --namespace=default
