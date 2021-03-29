# Building the images. It is necessary to build 2 images with different tags: latest and the SHA tag
# - The SHA tag is necessary to update the deployed image in the kubernetes cluster
# - The latest tag is a backup in case someone wants to deploy the latest image in the dev environment
docker build -t cristiangarciav/pokemonapi:latest -t cristiangarciav/pokemonapi:$SHA -f ./services/api/Dockerfile ./services/api

# Pushing both images to Docker Hub:
docker push cristiangarciav/pokemonapi:latest
docker push cristiangarciav/pokemonapi:$SHA

# Applying the Kubernetes config files in the Google Cloud  K8S cluster:
kubectl apply -f k8s
# Updating the new built image in Gooble Cloud K8S cluster:
kubectl set image deployments/api-deployment api=cristiangarciav/pokemonapi:$SHA